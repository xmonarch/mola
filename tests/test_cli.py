import unittest

from mola import runner


class TestCLIArguments(unittest.TestCase):
    parser = runner.parser()

    def test_defaults(self):
        args = self.parser.parse_args('input.jpg'.split())
        self.assertEqual("input.jpg", args.input)
        self.assertEqual(0.9, args.precision)
        self.assertIsNone(args.output)
        self.assertIsNone(args.theme)
        self.assertIsNone(args.colors)
        self.assertFalse(args.bg_center)
        self.assertFalse(args.bg_fill)
        self.assertFalse(args.bg_max)
        self.assertFalse(args.bg_scale)
        self.assertFalse(args.bg_tile)

    def test_theme(self):
        args = self.parser.parse_args('-t gruvbox -t nord input.jpg'.split())
        self.assertEqual("input.jpg", args.input)
        self.assertEqual("nord", args.theme)

        self._fail('-t unknown input.jpg')

    def test_colors(self):
        args = self.parser.parse_args('-t nord -c "#fff" -c "#e3e3e3" -c "#d5d5d5" -c "#ffff00" input.jpg'.split())
        self.assertEqual("input.jpg", args.input)
        self.assertEqual("nord", args.theme)
        self.assertEqual(4, len(args.colors))
        self.assertEqual("#fff", args.colors[0])
        self.assertEqual("#e3e3e3", args.colors[1])
        self.assertEqual("#d5d5d5", args.colors[2])
        self.assertEqual("#ffff00", args.colors[3])

        # validates HEX
        self._fail('-t nord -c "#fffz" input.jpg')

    def test_output(self):
        args = self.parser.parse_args('-o output.jpg input.jpg'.split())
        self.assertEqual("input.jpg", args.input)
        self.assertEqual("output.jpg", args.output)

        args = self.parser.parse_args('--bg-scale input.jpg'.split())
        self.assertEqual("input.jpg", args.input)
        self.assertIsNone(args.output)
        self.assertFalse(args.bg_center)
        self.assertFalse(args.bg_fill)
        self.assertFalse(args.bg_max)
        self.assertTrue(args.bg_scale)
        self.assertFalse(args.bg_tile)

        self._fail('-o output.jpg --bg-scale input.jpg')

    def _fail(self, command: str):
        try:
            _ = self.parser.parse_args(command.split())
            self.assertFalse(True, msg=f"Command '{command}' should have failed")
        except SystemExit:
            pass  # fails as expected


if __name__ == '__main__':
    unittest.main()