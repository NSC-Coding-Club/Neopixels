main = ["Swapped:"]

print("Hi! Please enter the text you want to use the app with.")
text = input()
print("What do you want to replace?")
toreplace = input()
print("Enter the text you want to replace", toreplace, "with.")
replacewith = input()
splittext = text.split(" ")
for i in splittext:
  if i in toreplace:
    print("found")
    main.append(i.replace(i, replacewith))
    print(main)
