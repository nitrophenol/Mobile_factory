from mobile_factory.enums import InputType, Component, ComponentType

PRICE_DATA = {
    InputType.A: 10.28,
    InputType.B: 24.07,
    InputType.C: 33.30,
    InputType.D: 25.94,
    InputType.E: 32.39,
    InputType.F: 18.77,
    InputType.G: 15.13,
    InputType.H: 20.00,
    InputType.I: 42.31,
    InputType.J: 45.00,
    InputType.K: 45.00,
    InputType.L: 30.00
}


COMPONENT_DATA = {
    InputType.A: Component.LED_SCREEN,
    InputType.B: Component.OLED_SCREEN,
    InputType.C: Component.AMOLED_SCREEN,
    InputType.D: Component.WIDE_ANGLE_CAMERA,
    InputType.E: Component.ULTRA_WIDE_ANGLE_CAMERA,
    InputType.F: Component.USB_C_PORT,
    InputType.G: Component.MICRO_USB_PORT,
    InputType.H: Component.LIGHTNING_PORT,
    InputType.I: Component.ANDROID_OS,
    InputType.J: Component.IOS_OS,
    InputType.K: Component.METALLIC_BODY,
    InputType.L: Component.PLASTIC_BODY
}

COMPONENT_TYPE = {
    InputType.A: ComponentType.SCREEN,
    InputType.B: ComponentType.SCREEN,
    InputType.C: ComponentType.SCREEN,
    InputType.D: ComponentType.CAMERA,
    InputType.E: ComponentType.CAMERA,
    InputType.F: ComponentType.PORT,
    InputType.G: ComponentType.PORT,
    InputType.H: ComponentType.PORT,
    InputType.I: ComponentType.OS,
    InputType.J: ComponentType.OS,
    InputType.K: ComponentType.BODY,
    InputType.L: ComponentType.BODY
}