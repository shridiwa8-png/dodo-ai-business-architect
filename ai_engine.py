"""
ai_engine.py - Core Execution Engine for DoDo V3
Integrates multi-format file parsing, intent routing, and resilient API fallbacks.
"""

from parser import parse_uploaded_file
from router import choose_prompt
from fallback import execute_gemini_request

def generate_recovery_plan(
    user_input: str,
    role: str = "Owner",
    tech_level: str = "Intermediate",
    tools: list = None,
    uploaded_files: list = None
) -> str:
    """
    Assembles user context, parses uploaded assets, picks dynamic prompt,
    and executes request via fallback engine.
    """
    if not user_input.strip() and not uploaded_files:
        return "⚠️ Please provide a business problem or upload a file/audio context."

    # 1. Select dynamic system prompt based on problem intent
    selected_prompt = choose_prompt(user_input)

    # 2. Extract and parse contents from uploaded files
    parsed_text_context = ""
    image_assets = []

    if uploaded_files:
        for file in uploaded_files:
            parsed_result = parse_uploaded_file(file)
            
            if parsed_result["type"] == "text":
                parsed_text_context += f"\n\n--- ATTACHED FILE DATA ({parsed_result['filename']}) ---\n"
                parsed_text_context += parsed_result["content"]
            elif parsed_result["type"] == "image":
                image_assets.append(parsed_result["content"])
            elif parsed_result["type"] == "error":
                parsed_text_context += f"\n\n⚠️ Error processing {parsed_result['filename']}: {parsed_result['content']}"

    # 3. Format user profile into clear instructions
    tools_str = ", ".join(tools) if tools else "None specified"
    
    full_prompt_text = f"""
{selected_prompt}

==============================
USER BUSINESS PROFILE
==============================
Role / Industry: {role}
Technical Confidence Level: {tech_level}
Current Software Stack / Tools: {tools_str}

==============================
ATTACHED DOCUMENT & FILE CONTEXT
==============================
{parsed_text_context if parsed_text_context else "No document text attached."}

==============================
BUSINESS PROBLEM / TASK
==============================
{user_input}
"""

    # 4. Construct payload for Gemini
    contents_payload = []
    
    # Add vision image assets if present
    for img in image_assets:
        contents_payload.append(img)
        
    contents_payload.append(full_prompt_text)

    # 5. Execute via Fallback Engine
    return execute_gemini_request(contents_payload)