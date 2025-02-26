import streamlit as st
from crewai.flow.flow import Flow, listen, start
from src.project11.agent1_main import outline_writer
from src.project11.agent2_main import writer
from reportlab.pdfgen import canvas  # For PDF creation

class ExampleFlow(Flow):

    @start()
    def writer_crew(self, topic):
        st.write("### First Agent is Running...")
        result = outline_writer(topic=topic)
        st.write("**Outline Generated:**")
        st.write(result.raw)
        
        if self.state is None:  # Ensure self.state is initialized
            self.state = {}
        self.state["outline"] = result.raw

    @listen("writer_crew")
    def writer_crew_listener(self):
        st.write("### Second Agent is Running...")
        result = writer(data=self.state["outline"])
        st.write("**Final Output:**")
        st.write(result.raw)

        if self.state is None:
            self.state = {}
        self.state["output"] = result.raw

    # @listen("writer_crew_listener")
    # def store_output(self):
    #     pdf_filename = "output.pdf"
    #     if self.state is None:
    #         self.state = {}

    #     c = canvas.Canvas(pdf_filename)
    #     c.drawString(100, 750, self.state["output"])  # Writing text on PDF
    #     c.save()

    #     st.write("Output stored in output.pdf")
    #     st.success("PDF generation successful.")
    #     st.balloons()

    #     self.state["pdf_filename"] = pdf_filename  # Save PDF filename in state

    # @listen("store_output")
    # def download_pdf(self):
    #     if self.state and "pdf_filename" in self.state:
    #         with open(self.state["pdf_filename"], "rb") as f:
    #             pdf_bytes = f.read()
    #         st.download_button("Download PDF", pdf_bytes, file_name="output.pdf", mime="application/pdf")

def kickoff(topic):
    poem_flow = ExampleFlow()
    poem_flow.writer_crew(topic)
    poem_flow.writer_crew_listener()
    # poem_flow.store_output()
    # poem_flow.download_pdf()

# Streamlit UI
st.title("AI Book Writer")

topic = st.text_input("Enter Topic:", "History of Islam")

if st.button("Generate Content"):
    kickoff(topic)
