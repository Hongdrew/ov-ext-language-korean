from pathlib import Path

import carb
import omni.kit.app
import omni.kit.test
import omni.kit.ui_test as ui_test
from omni.kit.mainwindow import get_main_window
from omni.kit.test_suite.helpers import get_test_data_path
from omni.ui.tests.compare_utils import CompareMetric
from omni.ui.tests.test_base import OmniUiTest


class TestLanguageKorea(OmniUiTest):
    # Before running each test
    async def setUp(self):
        omni.kit.window.preferences.show_preferences_window()

    # After running each test
    async def tearDown(self):
        omni.kit.window.preferences.hide_preferences_window()

    async def test_language_ui(self):
        # verify language ko_KR is known
        extension_path = omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module(__name__)
        expected_info = {
            "language_name": "Korean",
            "language_name_localized": "한국어",
            "pangram": "다람쥐 헌 쳇바퀴에 타고파",
            "font_path": f"{extension_path}/data/fonts/NotoSansKR-SemiBold.ttf",
            "font_scale": 1.2,
            "regions": [
                f"{extension_path}/data/regions/korean_001.txt",
                f"{extension_path}/data/regions/korean_002.txt",
                f"{extension_path}/data/regions/korean_003.txt",
                f"{extension_path}/data/regions/korean_004.txt",
                f"{extension_path}/data/regions/korean_005.txt",
            ],
            "font_overresolution_size": 66,
        }
        self.assertEqual(
            omni.kit.language.core.get_language_info(omni.kit.language.core.get_locale_id()), expected_info
        )

        # select language page
        pages = omni.kit.window.preferences.get_page_list()
        for page in pages:
            if page.get_title() == "Language":
                omni.kit.window.preferences.select_page(page)
                await ui_test.human_delay(50)

        # maximize window
        window = omni.ui.Workspace.get_window("Preferences")
        window.position_x = 0
        window.position_y = 0
        window.width = 1440
        window.height = 900
        await ui_test.human_delay(10)

        # verify golden image
        golden_img_dir = Path(get_test_data_path(__name__, "golden_img"))
        await self.finalize_test(
            golden_img_dir=golden_img_dir,
            golden_img_name="test_korea_font.png",
            cmp_metric=CompareMetric.MEAN_ERROR_SQUARED,
            hide_menu_bar=False,
        )
