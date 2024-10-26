import cli_menu


if __name__ == '__main__':
	options = [f'Option {i}' for i in range(1, 10)] + ['Exit']
	menu = cli_menu.CLIMenu(options=options)
	print(menu.wait_response())