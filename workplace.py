def alienPalindromes(names):
  # write your code here
  answer = ""

  for i in range(len(names)):
    name = names[i].replace(".", "").lower()

    if name == name[::-1]:
      answer += names[i] + "\n"

  return answer