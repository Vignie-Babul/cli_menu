import os


os.system('')


__all__ = [
	'colorize_hex'
]


def _hex_to_rgb(hex_):
	hex_code = hex_.lstrip('#')
	rgb_code = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
	return rgb_code

def colorize_hex(text: str, fg: hex = None, bg: hex = None) -> str:
	if fg is None:
		if bg is None:
			return text

	if bg is not None:
		bg_rgb = '\033[48;2;{};{};{}m'.format(*_hex_to_rgb(bg))
	else:
		bg_rgb = ''

	if fg is not None:
		fg_rgb = '\033[38;2;{};{};{}m'.format(*_hex_to_rgb(fg))
	else:
		fg_rgb = ''

	return f'{fg_rgb}{bg_rgb}{text}\033[0m'