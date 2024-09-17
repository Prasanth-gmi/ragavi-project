# import os
# from textwrap import dedent
# from crewai import Agent, Task, Crew
# from langchain_groq import ChatGroq
# from langchain.tools import Tool
# from tool import figma_create_file, figma_create_text_node, figma_export_png

# print("## Welcome to the Project")
# print("--------------------------")

# my_llm = ChatGroq(
#     api_key="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",
#     model="llama3-8b-8192",
# )

# project_type = input("What type of design would you like to build?\n")

# figma_access_token = "figd_1Uqsx3namEv48T9W8JjOEfKGIenVtfbjiwbNHGSk"

# input_md_file_path = "output/design.md"
# output_image_path = "output/design.png"

# tools = [
#     Tool(
#         name="Create Figma File",
#         func=lambda file_name, team_id=None: figma_create_file(figma_access_token, file_name, team_id),
#         description="Creates a new Figma file with the given name."
#     ),
#     Tool(
#         name="Create Text Node",
#         func=lambda file_key, text, x, y: figma_create_text_node(figma_access_token, file_key, text, x, y),
#         description="Creates a text node in the specified Figma file."
#     ),
#     Tool(
#         name="Export PNG",
#         func=lambda file_key, node_id, scale=1: figma_export_png(figma_access_token, file_key, node_id, scale),
#         description="Exports the specified Figma file as a PNG image."
#     )
# ]

# agent_Ragavi = Agent(
#     role="Stakeholder",
#     goal="Provide high-level project requirements and expectations.",
#     backstory="Experienced executive with a vision for the project's impact and success criteria.",
#     llm=my_llm,
# )

# agent_manikandan = Agent(
#     role="Product Owner",
#     goal="Translate stakeholder requirements into detailed product specifications.",
#     backstory=dedent("""\
#             As you have 3 years of experience in product management, you are responsible for defining the product vision,
#             creating the product backlog, and managing the team's progress towards the vision."""),
#     allow_delegation=True,
#     llm=my_llm,
# )

# agent_unesh = Agent(
#     role="UI/UX Designer",
#     goal="Create a visual representation of a login page in Figma based on Markdown content and export the design as an image.",
#     backstory="Seasoned UI/UX designer with 6 years of experience in creating engaging user experiences. Proficient in using Figma to transform written specifications into visually appealing and functional designs. Skilled in interpreting Markdown content and translating it into precise visual elements.",
#     llm=my_llm,
#     tools=tools
# )


# task1 = Task(
#         description=f"Define high-level requirements and success criteria for a {project_type} project.",
#         expected_output="A brief overview of project goals, target audience, and key features.",
#         agent=agent_Ragavi,
#         output_file='output/Stackeholder.md'
#     )

# task2 = Task(
#         description=f"Based on the stakeholder input, create detailed product specifications for the {project_type} project. Focus on user experience, key functionalities, and design elements. Include specific requirements for layout, color scheme, and any unique features of the {project_type}.",
#         expected_output="A comprehensive Markdown document containing detailed specifications, including user stories, acceptance criteria, design guidelines, and any technical considerations specific to the {project_type}.",
#         agent=agent_manikandan,
#         output_file=input_md_file_path
#     )

# task3 = Task(
#     description=dedent(f"""
#         1. Read the product specifications from: {input_md_file_path}
#         2. Create a new Figma file named "{project_type.capitalize()} Wireframe" using the Figma Create File tool.
#         3. Design a wireframe based on the specifications, focusing on layout and structure rather than detailed visuals.
#         4. Use the Figma Create Text Node tool to add labels and placeholder text.
#         5. Represent UI elements like buttons, input fields, and images as simple shapes.
#         6. Export the wireframe design as PNG using the Figma Export PNG tool to {output_image_path}
#         7. Verify that the image file has been created successfully.
#     """),
#     expected_output=f"A confirmation that the {project_type} wireframe has been created in Figma and exported to {output_image_path}.",
#     agent=agent_unesh,
#     output_file=output_image_path
# )
# crew = Crew(
#         agents=[agent_Ragavi, agent_manikandan, agent_unesh],
#         tasks=[task1,task2,task3],
#         verbose=2
# )
# try:
#     result = crew.kickoff()
#     print(result)

#     if os.path.exists(input_md_file_path):
#         print(f"Requirements file created successfully: {input_md_file_path}")
#         with open(input_md_file_path, 'r') as f:
#             print("Content of the requirements file:")
#             print(f.read())
#     else:
#         print(f"Failed to create requirements file: {input_md_file_path}")

#     if os.path.exists(output_image_path):
#         print(f"Design image created successfully: {output_image_path}")
#         print(f"Image size: {os.path.getsize(output_image_path)} bytes")
#     else:
#         print(f"Failed to create design image: {output_image_path}")

# except Exception as e:
#         print(f"An error occurred: {str(e)}")

# import os
# from textwrap import dedent
# from langchain.tools import Tool

#    ## Requirements

#     1. **Overall Structure:**
#        - Create a `<body>` with five `<div class="mobile-frame">` elements.
#        - Each `<div class="mobile-frame">` should represent a different screen:
#          - Contact List Screen
#          - Contact Details Screen
#          - Add/Edit Contact Screen
#          - Favorites Contacts Screen
#          - Recent Contacts Screen

# 2. **Mobile Frame Styling:**
#    - Each mobile frame should have a width of 360px and height of 640px.
#    - Apply a border (1px solid #ccc), rounded corners (10px), and a shadow (0 2px 4px rgba(0, 0, 0, 0.1)).
#    - Use Flexbox to position the frames horizontally within the viewport.

#     3. **HTML Elements:**
#    - Use `<header>` for the top bar with screen titles.
#    - Use `<main>` for the primary content area.
#    - Include `<section>` tags to group related content within each screen.
#    - Utilize form elements like `<input>`, `<button>`, and `<label>` where necessary.
#        - Include the following icons:
#          - Add Contact (rounded + icon): Bottom right of Contact List screen.
#          - Call Contact (phone icon): Below contact details in Contact Details screen.
#          - Message Contact (message icon): Below contact details in Contact Details screen.

#     4. **CSS Styling:**

#         - Include internal CSS within a `<style>` block in the `<head>`.
#         - Apply a consistent color scheme with the primary color being {primary_color} and the secondary color being {secondary_color}.
#         - Use the font family {font_family}.
#         - Style form inputs and buttons to be touch-friendly and responsive.
#         - Style icons with appropriate sizes and colors:
#             - Add Contact Icon: Primary color background {primary_color}, white color, position absolute to bottom right, border-radius: 50%, padding: 10px.
#             - Call Contact Icon: Primary color background {primary_color}, white color, position relative, border-radius: 50%, padding: 10px.
#             - Message Contact Icon: Primary color background {primary_color}, white color, position relative, border-radius: 50%, padding: 10px.

# 5. **Layout:**
#    - Use Flexbox for horizontal positioning of the mobile frames.
#    - Implement a 4-point spacing system for margin and padding.

#     6. **Mobile-Specific Features:**
#        - Each frame should have a header bar with a screen title.
#        - Display lists of contacts using unordered lists where applicable.
#        - Include interactive icons for functionality.

#     7. **Contact Details Screen:**
#         - Display contact details such as name, phone number.
#         - Center all contact details and icons.
#         - Include a call contact button (phone icon) and a message contact button (message icon) below the contact details.
#         - Display a call history section with the following details:
#             - Incoming, outgoing, and missed calls.
#             - Each call entry should include a call icon, call type, date, and time.

#     8. **Annotations:**
#        - Comment the HTML code to explain the purpose of each section.
#        - Comment the CSS to explain major styling rules.

#     9. **Responsive Design:**
#        - Use relative units for flexibility and ensure compatibility with various Android screen sizes.

#     ## Output Requirements
#         - Provide a HTML file with internal CSS.
#         - Include clear comments in both HTML and CSS.
#         - Ensure the design is mobile-friendly and accurately represents each screen as specified.
#     """,


# from crewai import Agent, Task, Crew
# from langchain_groq import ChatGroq
# from tool import read_content,write_content,clean_html,clean_css,main

# print("## Welcome to the HTML to Figma Wireframe Converter")
# print("------------------------------------------------------")

# my_llm = ChatGroq(
#     api_key="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",
#     model="llama-3.1-70b-versatile",
# )
# topic = input("Enter the topic for the design: ")
# # primary_color = input("Enter the primary color for the design: ")
# # secondary_color = input("Enter the secondary color for the design: ")
# # font_family = input("Enter the font family for the design: ")

# agent_Unesh = Agent(
#     role="UI/UX Designer",
#     goal=f"""Generate a HTML file that contains mobile-friendly wireframes for a {topic} using only HTML and CSS.""",
#     backstory="An experienced Designer with a strong background in UI/UX Design, specializing in translating HTML/CSS specifications into visual designs.",
#     llm=my_llm,
# )

# task1 = Task(
#     description=f"""Generate a single HTML file containing mobile wireframes for a {topic} application.""",
#     expected_output=f"""
#     Create a well-structured HTML file with mobile wireframes for a {topic} application, adhering to the following specifications:

#     1. Structure:
#        - Create a `<body>` with at least six `<div class="mobile-frame">` elements.
#        - Each `<div class="mobile-frame">` should represent a different screen relevant to the {topic} application.
#        - Always include Register and Login screens.
#        - The remaining screens should be specifically tailored to the {topic}.

#     2. Content:
#        - Register Screen: Include fields relevant to the {topic} (e.g., username, email, password, and any topic-specific fields).
#        - Login Screen: Include standard login fields and any {topic}-specific login options.
#        - Home Screen (Dashboard):
#          * Display a summary or overview specifically relevant to the {topic}.
#          * Include quick action buttons or links to main features of the {topic} application.
#          * Ensure the design is attractive and user-friendly for the specify {topic} applications.
#        - Additional Screens: Create at least seven more screens specific to the {topic} functionality.

#     3. Navigation:
#        - Use `<header>` for the top bar with screen titles.
#        - Use `<main>` for the primary content area.
#        - Include `<section>` tags to group related content within each screen.
#        - Utilize form elements like `<input>`, `<button>`, and `<label>` where necessary.
#        - Implement a consistent navigation menu (e.g., bottom tab bar or side menu).
#        - Include icons for home, list view, profile, and other topic-specific sections.

#     4. Style Link:
#        - Include a `<link>` tag in the `<head>` section of the HTML file to link to the external CSS file: `<link rel="stylesheet" href="wireframe_css2.css">`.

#     5. Class Names:
#        - Use descriptive class names for elements that will be styled in the CSS.
#        - Include classes like 'mobile-frame', 'nav-menu', 'button', 'input-field', etc.

#     6. Comments:
#        - Include detailed comments in the HTML explaining each section and any complex layout choices.
#        - Add comments suggesting potential variations or additional features specific to the {topic}.

#     The final output should be a single HTML file that, when opened in a browser and linked with the CSS file, displays a structured mobile wireframe for the {topic} application.
#     """,
#     agent=agent_Unesh,
#     tools = [main,read_content,write_content,clean_html,],
#     output_file="output/wireframe_html4.html"
# )

# task2 = Task(
#     description=f"""Generate a CSS file to style the HTML wireframes for a {topic} application.""",
#     expected_output=f"""
#     Create a well-structured CSS file to style the HTML wireframes for a {topic} application, adhering to the following specifications:

#     1. **Mobile Frame Styling:**
#        - Each mobile frame should have a width of 360px and height of 640px.
#        - Apply a border (1px solid #ccc), rounded corners (10px), and a shadow (0 2px 4px rgba(0, 0, 0, 0.1)).
#        - Use Flexbox to position the frames horizontally within the viewport.

#     2. Layout Styles:
#        - Implement a grid or flexbox layout for screen content.
#        - Style headers, main content areas, and footers consistently across frames.

#     3. Navigation Styles:
#        - Include internal CSS within a `<style>` block in the `<head>`.
#        - Style `.nav-menu` with appropriate background color, text color, and layout.
#        - Implement hover states for navigation links.

#     4. Button Styles:
#        - Style `.button` with background color, text color, padding, border radius, and hover states.

#     5. Form Styles:
#        - Style form elements (inputs, labels) for consistency and usability.

#     6. **Layout:**
#        - Use Flexbox for horizontal positioning of the mobile frames.
#        - Implement a 4-point spacing system for margin and padding.

#     7. Typography:
#        - Set a base font family and size.
#        - Define styles for headings, paragraphs, and other text elements.

#     8. Color Scheme:
#        - Use a color scheme appropriate for the {topic}, defining variables for primary color is green  and secondary colors is gray.

#     9. Responsive Design:
#        - Include media queries to ensure basic responsiveness for larger screens.

#     10. Comments:
#        - Include detailed comments explaining styling choices and any complex layout decisions.

#     The final output should be a CSS file that, when linked to the HTML file, provides a well-styled and functional mobile wireframe for the {topic} application.
#     """,
#     agent=agent_Unesh,
#     tools = [main,read_content,write_content,clean_css,],
#     output_file="output/wireframe_css4.css",
#     context = [task1]
# )


# crew = Crew(
#     agents=[agent_Unesh],
#     tasks=[task1,task2],
#     verbose=2
# )

# result = crew.kickoff()
# print(result)


import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from crewai import Crew
from agent import ProjectAgents
from task import ProjectTasks
from langchain_groq import ChatGroq
import uvicorn
from fastapi import FastAPI, Form, HTTPException, status


app = FastAPI()

my_llm = ChatGroq(
        api_key="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",
        model="llama-3.1-70b-versatile",
    )

agent = ProjectAgents()        
tasks = ProjectTasks()

@app.post("/designer/")
async def generate_design(
    topic: str = Form(...),
):
    try:
        unesh_agent = agent.unesh_agent(topic, my_llm)
        design_uiux_task1 = tasks.designer_task_html(unesh_agent, topic)
        design_uiux_task2 = tasks.designer_task_css(unesh_agent, topic, design_uiux_task1)

        crew = Crew(
            agents=[unesh_agent],
            tasks=[design_uiux_task1, design_uiux_task2],
            verbose=True,
        )
        
        try:
            result = crew.kickoff()
            print("Crew kickoff result:", result)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error during crew kickoff: {str(e)}"
            )
        if result:
            return {"message": "Design generated successfully", "result": result}
        else:
            raise HTTPException(status_code=500, detail="Failed to generate design")

    except Exception as e:
        print(f"Error in generate_design: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Design generator task error: {str(e)}"
        )
        
@app.get("/get-design/")
async def get_design():
    file_path = "outs/wireframe_html5.html"  
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        with open(file_path, 'r') as file:
            design_html = file.read()
        return HTMLResponse(content=design_html, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
