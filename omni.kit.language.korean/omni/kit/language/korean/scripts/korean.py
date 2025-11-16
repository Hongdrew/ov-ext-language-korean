import carb
import omni.ext

__all__ = ["KoreanLanguageExtension"]


class KoreanLanguageExtension(omni.ext.IExt):
    """
    Implementation of Korean font
    """

    def on_startup(self, ext_id):
        super().__init__()

        font_size = carb.settings.get_settings().get("/app/font/size")
        extension_path = omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module(__name__)
        omni.kit.language.core.register_language(
            ("ko_KR", "Korean", "한국어"),
            f"{extension_path}/data/fonts/NotoSansKR-SemiBold.ttf",
            1.2 if font_size == 14 or font_size == None else 1.0,
            [
                f"{extension_path}/data/regions/korean_001.txt",
                f"{extension_path}/data/regions/korean_002.txt",
                f"{extension_path}/data/regions/korean_003.txt",
                f"{extension_path}/data/regions/korean_004.txt",
                f"{extension_path}/data/regions/korean_005.txt",
            ],
            "다람쥐 헌 쳇바퀴에 타고파",
            font_overresolution_size=66,
        )

    def on_shutdown(self):
        omni.kit.language.core.unregister_language("ko_KR")
