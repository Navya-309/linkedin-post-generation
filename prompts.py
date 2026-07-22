from langchain.prompts import PromptTemplate

linkedin_prompt = PromptTemplate(
    input_variables=[
        "topic",
        "industry",
        "tone",
        "length",
        "audience",
        "emoji"
    ],

    template="""
You are a professional LinkedIn content creator.

Generate a LinkedIn post using:

Topic: {topic}
Industry: {industry}
Tone: {tone}
Length: {length}
Target Audience: {audience}
Use Emojis: {emoji}

Requirements:
1. Create a powerful hook.
2. Write engaging content.
3. Add storytelling if applicable.
4. Include a call-to-action.
5. Generate 5 relevant hashtags.
6. Make the content LinkedIn-friendly.

Return only the final LinkedIn post.
"""
)