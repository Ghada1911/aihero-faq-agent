import streamlit as st
import asyncio
from pathlib import Path
import json
import secrets
from datetime import datetime
from pydantic_ai import Agent
from pydantic_ai.messages import ModelMessagesTypeAdapter

# ----------------------
# Load your agent (faq_agent_v2 from Day 5)
# ----------------------
system_prompt = """
You are a helpful assistant for a course.  

Use the search tool to find relevant information from the course materials before answering questions.  

Always include references by citing the filename of the source material you used.  
When citing the reference, replace "faq-main" by the full path to the GitHub repository: "https://github.com/DataTalksClub/faq/blob/main/"
Format: [LINK TITLE](FULL_GITHUB_LINK)

If the search doesn't return relevant results, let the user know and provide general guidance.
""".strip()


def text_search(query: str):
    # Replace this with your actual search function
    return [{"filename": "faq-main/file1.md", "content": "Example content"}]


agent = Agent(
    name="faq_agent_v2",
    instructions=system_prompt,
    tools=[text_search],
    model='gpt-4o-mini'
)

# ----------------------
# Logging
# ----------------------
LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)


def log_interaction(agent, messages, source='user'):
    entry = {
        "agent_name": agent.name,
        "system_prompt": agent._instructions,
        "model": agent.model.model_name,
        "messages": ModelMessagesTypeAdapter.dump_python(messages),
        "source": source
    }
    ts = entry['messages'][-1]['timestamp']
    ts_str = ts.strftime("%Y%m%d_%H%M%S")
    rand_hex = secrets.token_hex(3)
    filename = f"{agent.name}_{ts_str}_{rand_hex}.json"
    filepath = LOG_DIR / filename
    with filepath.open("w", encoding="utf-8") as f_out:
        json.dump(entry, f_out, indent=2, default=str)
    return filepath


# ----------------------
# Streamlit UI
# ----------------------
st.set_page_config(page_title="FAQ Agent", page_icon="🤖", layout="centered")
st.title("🤖 FAQ Agent Interface")

st.write("Ask any question about the course, and the AI agent will answer using the course materials!")

user_input = st.text_input("Type your question here:")

if st.button("Send"):
    if user_input:
        with st.spinner("AI is thinking..."):
            result = asyncio.run(agent.run(user_prompt=user_input))

        st.markdown("### Answer:")
        st.write(result.output)

        # Optional: show references (if your output has them)
        if "https://github.com" in result.output:
            st.markdown("### References:")
            # Simple parse for links
            import re
            links = re.findall(r"https://github.com[^\s\]]+", result.output)
            for link in links:
                st.markdown(f"- [{link}]({link})")

        # Log the interaction
        log_interaction(agent, result.new_messages())
