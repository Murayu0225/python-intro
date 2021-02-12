print("こんにちは")
print("Pyhton自己紹介メーカーです。")
name=input("お名前は、何ですか？")
print(name+"さんですね！")
age=input(name+"さんは、何歳なんですか？")
if 100<=int(age):
  print("本当ですか？"+str(age)+"歳なんですね！")
elif 20<=int(age):
  print(str(age)+"歳ですね！")
elif 17==int(age):
  print(str(age)+"歳なんですか！？")
  print("私と同い年ですね！")
else:
  print("未成年の方ですね。"+str(age)+"歳ですね！")
print("なるほど。ここまでまとめると")
print("お名前は、"+name+"。年齢は、"+str(age)+"歳ですね！")
print("もう少し詳しく教えてください。")
hobby=input("趣味は、何でしょうか？")
print("趣味は、"+hobby+"ですね！")
print("質問に答えていただきありがとうございます。")
print("自己紹介文が完成しました。")
print("私は、"+name+"です。")
