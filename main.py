from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def main():
    # print("Hello from langchain-course!")
    print("Hello from langchain-course ( USING Google Gemini API)!")
    information = """
Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman, known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.
Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He received bachelor's degrees from the University of Pennsylvania in 1997 before moving to California, United States, to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.

In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research but later left; growing discontent with the organization's direction and their leadership in the AI boom in the 2020s led him to establish xAI. In 2022, he acquired the social network Twitter, implementing significant changes and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017.

Musk was the largest donor in the 2024 U.S. presidential election, and is a supporter of global far-right figures, causes, and political parties. In early 2025, he served as senior advisor to United States president Donald Trump and as the de facto head of DOGE. After a public feud with Trump, Musk left the Trump administration and announced he was creating his own political party, the America Party.

Musk's political activities, views, and statements have made him a polarizing figure, especially following the COVID-19 pandemic. He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation and promoting conspiracy theories, and affirming antisemitic, racist, and transphobic comments. His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service. His role in the second Trump administration attracted public backlash, particularly in response to DOGE.
"""

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template # ["information"] is a list containing the keys of what we're going to be filling and plugging in in runtime.
    ) 
    

    '''
     summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )  
    Here, we initialize an object of prompt templates. And we initialize it with the template. So this is the summary template that we wrote before. And then we give it input variables which is going to be a list containing the keys of what we're going to be filling and plugging in in runtime. And this should match the placeholders between the curly brackets {} that we have in our template here; that is: {information} 
    Now this is very much reminding us of an F string. And you might be thinking, why do we need all of this? And why don't we just use f strings instead? And this is because the prompt template is going to enforce that. We supply exactly the variables that we expect, and if we forget an input or misspell it, we get clean air instead sending us the broken prompt.
    It's also going to give us reusability and more clarity, because those prompts can become reusable in another langChain chain if we want to.
    And it's a first class citizen in link chain. It's also going to give us reusability and more clarity, because those prompts can become reusable in another langChain chain if we want to. And it's a first class citizen in langChain.

    So this means it's going to get logged, it's going to get traced. And we'll be showing this very very soon. And overall it's going to make our life debugging much more easier.
    '''
    
    '''
     let's now create a OpenAI chat model.

And I'm going to call it LLM.

And this is the way we're going to interact with the OpenAI model GPT five.

And this is what eventually is going to make the API calls to OpenAI to send the text and the prompts

and to get back the response from the LLM.

And who's going to pay for all those API calls?

And I remind you that in the previous video, we created an API key in OpenAI, which is connected to

our account with our payment information configured.

And the API key is stored in an environment variable, which is called OpenAI API key, which is loaded

into the runtime.

Now LangChain is going to search for this environment variable and is going to use this as credentials

to talk with OpenAI API.

And I give you an exercise.

Maybe if you want, you can check out the source code of the chat OpenAI model and see where it happens

there.

And we initialize the chat model with temperature equals to zero.

And temperature will control how random or creatives versus strict and deterministic the model response is going to be.

So low values between 0 and 0.3 is going to make the response deterministic, factual and probably repeatable.

And it's good for summarization, for code, for instructions, for test. And high values like above 0.8 until 1, will get us very creative results and it's good for poetry and fiction and out of the box ideas.

And if you're interested about how temperature works, then feel free to check out the theoretical section

where I explain this.

All right.

Let's go back to the code.

And the second argument that we give is going to be model equals to GPT five.
And now we're going to have a langChain ChatOpenAI object which eats under the hood, is going to be using the OpenAI SDK to make API calls to OpenAI with our API key.

    '''

    # llm = ChatOllama(temperature=0, model="gemma3:270m")
    # llm = ChatOpenAI(temperature=0, model="gpt-5") 
    llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.5-flash")

    
    '''
    And now we can go and create our first chain:
    
    chain = summary_prompt_template | llm

And we have the variable chain which is going to be summary prompt template the pipe operator.

And then ln.

So let me break down what's happening over here.

And we're using something which is called the LangChain Expression Language or LCEL.

And in this LCEL (LangChain Expression Language) syntax we create a chain by composing two components a prompt_template and a large language

model (llm).

Now the prompt_template is going to come from the variable summary_prompt_template.

And this is going to format input variables.

And in this case information into a prompt string which will eventually be propagated to the LLM, and

the LM variable is a chat open AI object, which takes in an input a prompt string and generates a text

response.

Now, this pipe operator (|) langChain Expression Language is going to create a new runnable chain.

So this is a new term runnable by connecting the output of the left component as an input to the right component.

So summary_prompt_template pipe llm means that we first want to format the input using the prompt template,

and then to pass the resulting prompt string into the LLM to generate the response.

So the resulting chain is called a runnable object.

So this means we can invoke it using the invoke method with some input variables matching the prompt template.

And here in this case it's going to be information.
    '''
    
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

'''
So we just need to know from a very high level that we read these from left to right here: chain = summary_prompt_template | llm

And here we are plugging in the result of formatting the prompt template into the LLM.

So when do we run this.

So we do this using the invoke method that the runnable interface has.

So what's going to happen here is that when we run chain dot  i.e, chain.invoke() we actually going to invoke the

invoke method of the summary_prompt_template which is a class of prompt template.

And when we invoke it, we're going to give it the input of the information key to be holding the information

value. i.e., {"information": information} in the line: response = chain.invoke(input={"information": information})

And in this case it's going to be the Elon Musk information.

So once we do that then we're going to create a prompt value, which is sort of like a fancy word of

saying a string.

And that string is going to be piped to the LLM method.

And this pipe is actually some very clever way to go and call the LLM invoke method, which it has with

the input to be the prompt value.

So the final prompt that we want to send to the LLM.

So this is just a clever way to chain everything up together and hence the name of langchain.

So eventually when we're going to run this code we are going to take this string that you see right

over here..>>>>>
summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

We're going to plug in the information of Elon Musk.

And this string is what is going to be sent eventually to the LLM.

Right.

So I know it sounded at the beginning very, very complicated.

But actually what it's doing is quite simple.

And in the next video we're also going to be tracing this and see the exact objects and debugging it.

So don't worry, you will understand this.

And I think this is the hardest concept to comprehend in langChain and the langChain Expression

Language.

And it is totally okay that you do not understand it by now.

And just a fun fact, even implementing and understanding how agents work is going to be much easier

than understanding this piping operator in the chain expression language.

All right, so just to summarize the code here, all you need to understand is that we're taking the

variable of information.

We're plugging it in to this string over here.

And we're dynamically going to put the value of the information about Elon Musk.

And this is the string that we're going to be sending eventually to the LLM and get a response to it.

Right.

So this is everything you need to know from this video.



All right.

So let me go now and finally run this code and let's see what results do we get.

And I'm going to fast forward it a bit because we're going to use GPT five And GPT five is a bit slow LLM it's very capable but it's very slow.

So let me go fast forward it.

And at the end we're going to print response dot content, which is going to be the final string that

the LLM returns.

So we'll be debugging and we'll be tracing all of this in the next video.

So let's just wait to see the output.

All right so we can see now the short summary.

And we can see now two interesting facts on Elon Musk.

So this looks great.

And now you can read it in your own time.

And in the next video we're going to be debugging this.

We're going to be examining the objects.

And we are going to be tracing it with Lindsmith.
'''
if __name__ == "__main__":
    main()

###################################################################################################################

#CHECKING IF THE ENVIRONMENT VARIABLE IS SET UP PROPERLY BY TYPING THE BELOW COMMAND IN THE TERMINAL
'''

python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('GEMINI_API_KEY'))"

'''
# OUTPUT: 
'''
(langchain-course) PS C:\LangChain_Course> python -u "c:\LangChain_Course\template_tut.py"
Hello from langchain-course ( USING Google Gemini API)!
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1759845525.884568   11540 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.
Here's a summary and two interesting facts about Elon Musk, based on the provided information:












**Short Summary:**
Elon Musk, born June 28, 1971, in South Africa, is a prominent businessman and the world's wealthiest person since 2021, with an estimated net worth of $424.7 billion as of May 2025. He is known for leading companies such as Tesla, SpaceX, and X (formerly Twitter). After co-founding Zip2 and X.com (which evolved into PayPal), he founded SpaceX in 2002 and became CEO of Tesla in 2008. His other ventures include Neuralink, The Boring Company, and AI companies OpenAI (which he left) and xAI. A polarizing figure, Musk has been involved in significant political activities, including serving as de facto head of the Department of Government Efficiency (DOGE) in the Trump administration before founding his own "America Party." He has faced criticism for unscientific statements, promoting conspiracy theories, and the increase of hate speech on X.     

**Two Interesting Facts:**

1.  Musk served as the de facto head of the "Department of Government Efficiency (DOGE)" in the Trump administration in early 2025, but after a public feud with President Trump, he left and announced he was creating his own political party, the "America Party."
2.  He initially co-founded OpenAI to advance artificial intelligence research but later left due to "growing discontent with the organization's direction" and subsequently established his own AI company, xAI.
'''