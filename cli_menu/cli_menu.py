from cli_menu import (
	win_key,
	color
) 

import os


__all__ = [
	'CLIMenu'
]


class CLIMenu:
	def __init__(
		self,
		options: list,
		highlight_length: int = 12,
		last_option_exit: bool = True,
		fg: hex = '#ffffff',
		bg: hex = '#3d7efc',
	) -> None:

		self._options = options
		self._highlight_length = highlight_length
		self._last_option_exit = last_option_exit
		self._fg = fg
		self._bg = bg

		self._current_option_index = 0
		self._options_length = len(self._options) - 1
		self._pointer = '> '
		self._pointer_colored = color.colorize_hex(
			text=self._pointer,
			bg=self._bg
		)
		self._no_pointer = '  '

	def _manage_option_color(self, option_index):
		bg = None
		if option_index == self._current_option_index:
			bg = self._bg

		return bg

	def _set_pointer(self, option_index, option):
		if option_index == self._current_option_index:
			return self._pointer_colored + option

		return self._no_pointer + option

	def _display(self):
		for index, option in enumerate(self._options):
			option_colored = color.colorize_hex(
				text=option + ' ' * (self._highlight_length-len(option)),
				fg=self._fg,
				bg=self._manage_option_color(option_index=index)
			)
			formatted_option = self._set_pointer(
				option_index=index,
				option=option_colored
			)
			print(formatted_option)

	def _raise_current_option(self):
		if self._current_option_index > 0:
			self._current_option_index -= 1

	def _lower_current_option(self):
		if self._current_option_index < self._options_length:
			self._current_option_index += 1

	def _exit(self):
		if not self._last_option_exit:
			return self._options[self._current_option_index]

		if self._current_option_index == self._options_length:
			return None
		else:
			return self._options[self._current_option_index]

	def wait_response(self):
		while True:
			os.system('cls')

			self._display()

			key = win_key.read_key_input()
			match key:
				case win_key.SpecialFunctionKeys.ESC:
					return None
				case win_key.SpecialFunctionKeys.UP:
					self._raise_current_option()
				case win_key.SpecialFunctionKeys.DOWN:
					self._lower_current_option()
				case win_key.SpecialFunctionKeys.ENTER:
					return self._exit()
				case _:
					pass