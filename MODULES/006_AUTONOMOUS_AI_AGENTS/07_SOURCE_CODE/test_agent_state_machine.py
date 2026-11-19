import unittest
from agent_state_machine import BoundedAgent


class TestBoundedAgent(unittest.TestCase):
    def test_completed_plan(self):
        ag = BoundedAgent({"echo": lambda s: s.upper()}, max_steps=3)
        r = ag.run([{"tool": "echo", "arg": "hello"}])
        self.assertEqual(r["status"], "COMPLETED")
        self.assertEqual(r["trace"][0]["observation"], "HELLO")

    def test_blocks_untrusted_tool(self):
        ag = BoundedAgent({"safe": lambda s: s}, max_steps=3)
        r = ag.run([{"tool": "rm_rf", "arg": "/"}])
        self.assertEqual(r["status"], "BLOCKED_UNTRUSTED_TOOL")

    def test_budget_limit(self):
        ag = BoundedAgent({"noop": lambda s: s}, max_steps=1)
        r = ag.run([{"tool": "noop", "arg": "1"}, {"tool": "noop", "arg": "2"}])
        self.assertEqual(r["status"], "BUDGET_EXCEEDED")


if __name__ == "__main__":
    unittest.main()
