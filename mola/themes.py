from typing import List, Dict

from colour import Color

from mola.utils import print_theme, gray


def of(colors: List[str]) -> List[Color]:
    """
    Convert list of HEX color representations into a list of color objects
    :param colors: list of HEX colors for a theme
    :return: list of colour.Color object
    """
    return [Color(color_hex) for color_hex in set(colors)]


# List of known color themes
THEMES: Dict[str, List[str]] = dict()
BY: Dict[str, str] = dict()

THEMES['nord'] = ['#2e3440', '#3b4252', '#434c5e', '#4c566a', '#d8dee9', '#e5e9f0', '#eceff4', '#8fbcbb', '#88c0d0',
                  '#81a1c1', '#5e81ac', '#bf616a', '#d08770', '#ebcb8b', '#a3be8c', '#b48ead']
BY['nord'] = 'https://www.nordtheme.com/'

THEMES['gruvbox'] = ['#282828', '#cc241d', '#98971a', '#d79921', '#458588', '#b16286', '#689d6a', '#a89984', '#928374',
                     '#fb4934', '#b8bb26', '#fabd2f', '#83a598', '#d3869b', '#8ec07c', '#ebdbb2', '#1d2021', '#3c3836',
                     '#504945', '#665c54', '#7c6f64', '#928374', '#d65d0e', '#32302f', '#bdae93', '#d5c4a1', '#ebdbb2',
                     '#fbf1c7', '#fe8019']
BY['gruvbox'] = 'https://github.com/morhetz/gruvbox'

THEMES['solarized'] = ['#1c1c1c', '#262626', '#585858', '#626262', '#808080', '#8a8a8a', '#e4e4e4', '#ffffd7',
                       '#af8700', '#d75f00', '#d70000', '#af005f', '#5f5faf', '#0087ff', '#00afaf', '#5f8700']
BY['solarized'] = 'https://ethanschoonover.com/solarized/'

THEMES['challenger-deep'] = ['#cbe3e7', '#1b182c', '#fbfcfc', '#100e23', '#565575', '#ff8080', '#ff5458', '#95ffa4',
                             '#62d196', '#ffe9aa', '#ffb378', '#91ddff', '#65b2ff', '#c991e1', '#906cff', '#aaffe4',
                             '#63f2f1', '#cbe3e7', '#a6b3cc']
BY['challenger-deep'] = 'https://challenger-deep-theme.github.io/'

THEMES['dracula'] = ['#f8f8f2', '#000000', '#4d4d4d', '#ff5555', '#ff6e67', '#50fa7b', '#5af78e', '#f1fa8c', '#f4f99d',
                     '#bd93f9', '#caa9fa', '#ff79c6', '#ff92d0', '#8be9fd', '#9aedfe', '#bfbfbf', '#e6e6e6', '#282a36']
BY['dracula'] = 'https://draculatheme.com'


def preview_themes():
    """
    Prints list of all themes available in the configuration
    """
    for theme_name in THEMES.keys():
        print(f"{theme_name} (credit: {BY[theme_name]})")
        theme = of(THEMES[theme_name])
        theme.sort(key=lambda c: gray(c))
        print_theme(theme, block_size=4, line_size=4 * 256 + 1)
        print()
        print()
