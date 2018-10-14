#py the hard way
#ex28

# - *- coding: utf- 8 - *-

print("1. True and True", ":", "My answer is", True, "; Actual answer is", True and True)

print("2. False and True", ":", "My answer is", False , "; Actual answer is", False and True)

print("3. 1 == 1 and 2 == 1", ":", "My answer is", False, "; Actual answer is", 1 == 1 and 2 == 1)

print("4. \"test\" == \"test\"", ":", "My answer is", True, "; Actual answer is", "test" == "test")

print("5. 1 == 1 or 2 != 1", ":", "My answer is", True, "; Actual answer is", 1 == 1 or 2 != 1)

print("6. True and 1 == 1", ":", "My answer is", True, "; Actual answer is", True and 1 == 1)

print("7. False and 0 != 0", ":", "My answer is", False, "; Actual answer is", False and 0 != 0)

print("8. True or 1 == 1", ":", "My answer is", True, "; Actual answer is", True or 1 == 1)

print("9. \"test\" == \"testing\"", ":", "My answer is", False, "; Actual answer is", "test" == "testing")

print("10. 1 != 0 and 2 == 1", ":", "My answer is", True, "; Actual answer is", 1 != 0 and 2 == 1)

print("11. \"test\" != \"testing\"", ":", "My answer is", True, "; Actual answer is", "test" != "testing")

print("12. \"test\" == 1", ":", "My answer is", False, "; Actual answer is", "test" == 1)

print("13. not (True and False)", ":", "My answer is", True, "; Actual answer is", not (True and False))

print("14. not (1 == 1 and 0 != 1)", ":", "My answer is", False, "; Actual answer is", not (1 == 1 and 0 != 1))

print("15. not (10 == 1 or 1000 == 1000)", ":", "My answer is", False, "; Actual answer is", not (10 == 1 or 1000 == 1000))

print("16. not (1 != 10 or 3 == 4)", ":", "My answer is", False, "; Actual answer is", not (1 != 10 or 3 == 4))

print("17. not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")", ":", "My answer is", True, "; Actual answer is", not ("testing" == "testing" and "Zed" == "Cool Guy"))

print("18. 1 == 1 and (not (\"testing\" == 1 or 1 == 0))", ":", "My answer is", True, "; Actual answer is", 1 == 1 and (not ("testing" == 1 or 1 == 0)))

print("19. \"chunky\" == \"bacon\" and (not (3 == 4 or 3 == 3))", ":", "My answer is", False, "; Actual answer is", "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))

print("20. 3 == 3 and (not (\"testing\" == \"testing\" or \"Python\" == \"Fun\"))", ":", "My answer is", False, "; Actual answer is", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))