from datetime import datetime

user_input = ["hi", "hello", "chào", "xin chào"]
user_time = [
  "hôm nay ngày mấy?",
  "ngày hôm nay",
  "ngày mấy?",
  "time?",
  "time",
  "What time is it?",
  "What time is it",
  "What's the time",
  "What's the time?"
]

# input emoji
emoji_input_hello = ["🤗"]
emoji_input_like = ["❤️", "✔️", "👌", "👍", "🎉"]
emoji_input_bad = ["😞", "🤦‍♀️", "☹️", "👎"]

# bot rep
bot_rep = "hi bro :)" 
bot_rep_like = "Thanks bro (^_^)"
bot_rep_bad = "Sorry bro :v"

def sample_response(input):
  user_mess = str(input).lower()

  if user_mess in (user_input):
    return bot_rep
  elif user_mess in (emoji_input_hello):
    return bot_rep
  elif user_mess in (emoji_input_like):
    return bot_rep_like
  elif user_mess in (emoji_input_bad):
    return bot_rep_bad  
  elif user_mess in (user_time):
    now = "Today is: " + datetime.now().strftime("%d-%m-%y, %H:%M:%S")
    return str(now)
  # Có thể thêm các câu hỏi mà người dùng nhập vào ở đây
  # Có thể chỉnh sữa nếu bạn biết về Python
  
  return "Ask something else bro? It's okay to ask such a difficult question :<"
