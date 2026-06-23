import os
import gradio as gr
from google import genai
from dotenv import load_dotenv

load_dotenv()

def run_interview_bot(job_domain, current_question, user_answer, action_type):
    # Quick check so we don't waste an API call if they click evaluate on nothing
    if action_type == "Evaluate Answer" and not user_answer.strip():
        return "⚠️ Validation Error: Please type an answer in the text box before submitting for evaluation!"
    
    try:
        client = genai.Client()
        
        if action_type == "Generate Question":
            prompt = f"Generate one challenging entry-level technical interview question for a {job_domain} role. Do not provide the answer."
            system_instruction = "You are a senior technical interviewer at a top tech company. Be concise, realistic, and highly professional."
        else: 
            # Now passing both the question and the answer so the AI can grade properly!
            prompt = f"""
            The candidate is applying for a {job_domain} role.
            Interview Question asked: '{current_question}'
            Candidate's Answer: '{user_answer}'
            
            Evaluate this answer. Provide a score out of 10, list what key points were missing, and give a great ideal answer.
            """
            system_instruction = "You are an expert technical interviewer. Provide critical, constructive feedback, scoring rigorously like a real manager."

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={"system_instruction": system_instruction, "temperature": 0.7}
        )
        return response.text
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return f"Cloud Connection Timeout: Please check your terminal or API key. Details: {e}"

# UI Layout Using Gradio Blocks
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🏢 Real-Time AI Technical Interview Simulator")
    gr.Markdown("Select your target tech domain, generate a live question, and test your readiness.")
    
    with gr.Row():
        with gr.Column():
            domain_input = gr.Dropdown(
                label="Target Engineering Role", 
                choices=["Python Developer Intern", "Backend Engineer", "Data Analyst", "Frontend Developer"],
                value="Python Developer Intern"
            )
            question_btn = gr.Button("🎯 Generate Interview Question", variant="secondary")
            question_output = gr.Textbox(label="Current Interview Question", interactive=False, lines=4)
            
        with gr.Column():
            answer_input = gr.Textbox(label="Your Answer", placeholder="Type your detailed code or conceptual explanation here...", lines=5)
            submit_answer_btn = gr.Button("📊 Submit Answer for Evaluation", variant="primary")
            feedback_output = gr.Textbox(label="Detailed Performance Review & Score", interactive=False, lines=6)

    # 1. Generate Question Button Click
    question_btn.click(
        fn=lambda domain: run_interview_bot(domain, "", "", "Generate Question"), 
        inputs=domain_input, 
        outputs=question_output
    )
    
    # 2. Fixed Submit Answer Button Click (Now sending all 4 positional parameters!)
    submit_answer_btn.click(
        fn=lambda domain, q, ans: run_interview_bot(domain, q, ans, "Evaluate Answer"), 
        inputs=[domain_input, question_output, answer_input], 
        outputs=feedback_output
    )

if __name__ == "__main__":
    demo.launch()