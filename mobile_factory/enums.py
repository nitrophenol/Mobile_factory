from enum import Enum, auto


class BaseEnum(Enum):
    @classmethod
    def get_values(cls):
        return [(enum.name, enum.value) for enum in cls]
    
    @classmethod
    def get_keys(cls):
        return [enum.name for enum in cls]
    
    @classmethod
    def get_values_list(cls):
        return [enum.value for enum in cls]

class InputType(BaseEnum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()
    G = auto()
    H = auto()
    I = auto()
    J = auto()
    K = auto()
    L = auto()

    @classmethod
    def get_values(cls):
          return [(input_type.name, input_type.value) for input_type in cls]


class Component(BaseEnum):
    LED_SCREEN = "LED Screen"
    OLED_SCREEN = "OLED Screen"
    AMOLED_SCREEN = "AMOLED Screen"
    WIDE_ANGLE_CAMERA = "Wide-Angle Camera"
    ULTRA_WIDE_ANGLE_CAMERA = "Ultra-Wide-Angle Camera"
    USB_C_PORT = "USB-C Port"
    MICRO_USB_PORT = "Micro-USB Port"
    LIGHTNING_PORT = "Lightning Port"
    ANDROID_OS = "Android OS"
    IOS_OS = "iOS OS"
    METALLIC_BODY = "Metallic Body"
    PLASTIC_BODY = "Plastic Body"

class ComponentType(BaseEnum):
    SCREEN = "Screen"
    CAMERA = "Camera"
    PORT = "Port"
    OS = "OS"
    BODY = "Body"
