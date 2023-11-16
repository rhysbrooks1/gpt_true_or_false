from openai import OpenAI

#key
client = OpenAI(
api_key = 'enter api key here'
)

print("enter your message")

def getResponse():

    userInput = input()
    system_message = "You are a helpful assistant that answers questions with exclusively 'True' or 'False' as one word answers based on whether or not something is true."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": userInput},
        ],
    )
    return response

response_message = getResponse().choices[0].message.content

while response_message.lower() == 'true.' or response_message.lower() == 'true.':
    print(response_message)
    response_message = getResponse().choices[0].message.content
    print("enter next statement")

else:
    print(response_message)
