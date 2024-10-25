import enum
import msvcrt


__all__ = [
	'SpecialFunctionKeys',
	'read_key_input'
]


class SpecialFunctionKeys(enum.Enum):
	ENTER = b'\r'
	TAB = b'\t'
	SLASH = b'\\'
	ESC = b'\x1b'
	BACKSPACE = b'\x08'

	RIGHT = b'\xe0M'
	LEFT = b'\xe0K'
	UP = b'\xe0H'
	DOWN = b'\xe0P'
	DELETE = b'\xe0S'
	HOME = b'\xe0G'
	END = b'\xe0O'
	PG_UP = b'\xe0I'
	PG_DN = b'\xe0Q'


def _get_key() -> bytes:
	return msvcrt.getch()

def _match_key(key: bytes) -> SpecialFunctionKeys | None:
	for special_function_key in SpecialFunctionKeys:
		if key == special_function_key.value:
			return special_function_key

	return None

def _get_special_key(key: bytes) -> SpecialFunctionKeys | str | None:
	if key == b'\xe0':
		key += _get_key()
		return _match_key(key)

	if str(key).startswith("b'\\"):
		return _match_key(key)

	try:
		return key.decode('utf-8')
	except UnicodeDecodeError:
		return key

def read_key_input() -> SpecialFunctionKeys | str | None:
	key = _get_key()
	if not key:
		return None
	return _get_special_key(key)