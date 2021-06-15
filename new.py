import os
from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage,
os

app = Flask(__name__)

line_bot_api = LineBotApi('l1mTywei3CSnlbH0Oc4RvGf5tT4l9Z96Ne5aq1EWSWWcWfe2EbezTw2Kvn6O1MUDrPlQ0N0kYkBZ7Xzp52bjvc9BZ4BC0I0AMwAg5zXOMFktsiqdldHTlgS13ADhlbePRWL/xVLhuitkGRhpdPl+2AdB04t89/1O/w1cDnyilFU=
')
handler = WebhookHandler('b74aafd355499451b39f5631856dbc70')


@app.route("/callback", methods=['POST''GET'])
def callback():
	# Get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']

	# Get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	# Handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)

	return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	""" Here's all the messages will be handled and processed by the program """

	msg = (event.message.text).lower ()

	if 'wkwk' in msg:
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Bah ketawa"))
	elif '/join' in msg:
		msg.replace('/join')
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Set your id name first."))
	elif '/setname ' in msg:
		name = msg.replace('/setname','')
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Your name is", name,". Then set your current level")
	elif '/setlevel ' in msg:
        currentlevel = msg.replace('/setlevel','')
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="Your name is", name,"and your level is", currentlevel)
	elif '/myprofile' in msg:
		profile = [[name], [currentlevel]]
		for inner_list in profile:
			for profile in inner_list:
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text=profile, end=" ")
		TextSendMessage()


	else :
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text=event.message.text)




 


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
