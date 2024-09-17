# from dotenv import load_dotenv
# load_dotenv()
# from crewai import Crew
# from langchain_community.llms import Ollama
# from agent import ProjectAgents
# from task import ProjectTasks
# # from tools import ProjectTools
# from langchain_groq import ChatGroq
# from crewai.process import Process

# print("## Welcome to the HTML to Figma Wireframe Converter")
# print("------------------------------------------------------")

# my_llm = ChatGroq(
#     api_key="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",
#     model="llama-3.1-70b-versatile",
# )
# topic = input("Enter the topic for the design: ")


# agents = ProjectAgents(my_llm)
# tasks = ProjectTasks()

# unesh_agent = agents.unesh_agent(my_llm)


# design_uiux_task = tasks.uiux_task(unesh_agent,topic)
# - **User Management Screen:**
#     * Add sections for adding tenants, tenant products.
#     * Include forms with relevant fields (e.g., tenant name, product name, and tenant/product dropdown selections).
# - **Task/product   Management Screen:** Display a list of tasks related to tenant and product management.

# Crew = Crew(
#     agents=[

#     ],
#     tasks=[

#     ],
#     verbose=True,
#     process=Process.sequential,
#     manager_llm=my_llm,
# )

# result = Crew.kickoff()
# print(result)


# from textwrap import dedent
# from crewai import Task
# from tool import main, read_content, write_content, clean_html, clean_css


# class ProjectTasks():
#     def designer_task_html(self, agent, topic):
#         return Task(
#             description=f"""Generate a single HTML file containing mobile wireframes for a {topic} application.""",
#             expected_output=f"""
#             Create a well-structured HTML file with mobile wireframes for a Tenant Management Dashboard application, adhering to the following specifications:

#             1. Structure:
#             - Create a `<body>` with at least eight `<div class="mobile-frame">` elements.
#             - Each `<div class="mobile-frame">` should represent a different screen relevant to the {topic} application.
#             - Always include Login, and Dashboard screens.
#             - The remaining screens should be specifically tailored to the {topic}, including User Management and Policy Setup.

#             2. Content:
#             - **Login Screen:** Include fields for username, password, and a submit button.
#             - **Dashboard Screen:** Provide a sidebar menu with links for HR Recruitment, Employee Onboarding, Payroll Process, Admin Setting, and View Reports. Include a table for managing permissions with checkboxes.
#             - **Product List Screen:** Display all list of available products mentioned here like Human Resources (HR), Finance and Accounting, Marketing and Sales,Operations, Customer Service.
#             - **Create Role Screen:** Include a form for entering a role name and a submit button.
#             - **Role List Screen:** Display all the of roles mentioned here like Admin, HR, Manager,Employee,Manager/Supervisor,Training Manager in li tag all should print.
#             - **Create Resource Screen:** Include a form for entering permission names and a submit button.
#             - **Resource List Screen:** Display a list of permissions like HR Recruitment, Employee Onboarding, and Payroll Process.
#             - **Roles & Permissions Screen:** Provide a table with checkboxes for various permissions like Add,Edit,view and actions for different roles like Admin,HR manager.give me 4 to 5 element defines a table cell.
#             - **Add Tenant Screen:** Include a form for entering tenant names and a submit button.
#             - **Reports Screen:** Display a list of report types.
#             - **Settings Screen:** Include options for account and system settings.

#             3. Navigation:
#             - Use `<header>` for the top bar with screen titles.
#             - Use `<main>` for the primary content area.
#             - Include `<section>` tags to group related content within each screen.
#             - Utilize form elements like `<input>`, `<button>`, `<label>`, and `<select>` where necessary.
#             - Implement a consistent navigation menu (e.g., bottom tab bar or side menu).

#             4. Style Link:
#             - Include a `<link>` tag in the `<head>` section of the HTML file to link to the external CSS file: `<link rel="stylesheet" href="wireframe_css6.css">`.

#             5. Class Names:
#             - Use descriptive class names for elements that will be styled in the CSS.
#             - Include classes like 'mobile-frame', 'nav-menu', 'button', 'input-field', etc.

#             6. Comments:
#             - Include detailed comments in the HTML explaining each section and any complex layout choices.
#             - Add comments suggesting potential variations or additional features specific to the {topic}.

#             The final output should be a single HTML file that, when opened in a browser and linked with the CSS file, displays a structured mobile wireframe for the {topic} application.
#             """,
#                 output_file="outs/wireframe_html6.html",
#                 tools=[main, read_content, write_content, clean_html],
#                 agent=agent,
#             )

#     def designer_task_css(self, agent, topic, context):
#         return Task(
#             description=f"""Generate a CSS file to style the HTML wireframes for a {topic} application.""",
#             expected_output=f"""
#                 Create a well-structured CSS file to style the HTML wireframes for a {topic} application, adhering to the following specifications:

#                 1. **General Styling:**
#                 - Use the `box-sizing: border-box;` property globally to ensure padding and border are included in the element's total width and height.
#                 - Reset margin and padding to zero for all elements to ensure consistent styling.

#                 2. **Body:**
#                 - Set the font family to Arial, sans-serif.
#                 - Use Flexbox to center content both horizontally and vertically.
#                 - Apply a light background color (#f4f4f4) and add padding of 20px around the body.

#                 3. **Mobile Frame:**
#                     - Define a `.mobile-frame` class with:
#                     - Width: 360px
#                     - Height: 640px
#                     - Border: 1px solid #ccc
#                     - Border-radius: 10px
#                     - Box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)
#                     - Background color: #fff
#                     - Margin: 10px
#                     - Padding: 20px
#                     - Overflow-y: auto

#                 4. **Typography:**
#                 - Set styles for headings (`h1`, `h2`, `h3`, etc.) with bold font-weight and appropriate font sizes.
#                 - Define styles for paragraphs with a bottom margin of 20px.

#                 5. **Layout Styles:**
#                 - Style the `header` with a background color (#4CAF50), white text color, and centered text.
#                 - Style the `main` and `section` elements with padding and background colors. Add shadows and borders for separation.

#                 6. **Navigation:**
#                 - Style `.nav-menu` to be fixed at the bottom of the viewport with a background color (#4CAF50) and centered text.
#                 - Style navigation links with white text and include hover effects.
#                 - Style `.sidebar` to slide in and out with smooth transitions.
#                 - Implement a `.menu-toggle` button for toggling the sidebar visibility.

#                 7. **Buttons:**
#                 - Style `.button` with a green background, white text, padding, border-radius, and hover effects.

#                 8. **Form Elements:**
#                 - Style form elements (`input`, `select`, etc.) with consistent padding, margin, border, and border-radius.

#                 9. **Color Scheme:**
#                 - Define CSS variables for primary color (#4CAF50) and secondary color (#ccc).

#                 10. **Responsive Design:**
#                 - Add media queries to ensure the `.mobile-frame` styles adapt for larger screens.
#                 - Implement a media query for screens with a minimum width of 768px:
#                 - Within the media query, adjust the `.mobile-frame` class to:
#                         - Width: 360px
#                         - Height: 640px
#                         - Remove the border by setting `border: none;`.
#                         - Remove the box shadow by setting `box-shadow: none;`

#                 11. **Comments:**
#                 - Include comments in the CSS file to explain the styling choices and any complex layout decisions.

#                 The final CSS file should be linked to the HTML and provide a well-styled and functional mobile wireframe for the {topic} application.
#                 """,
#             output_file="outs/wireframe_css6.css",
#             context=[context],
#             tools=[main, read_content, write_content, clean_css],
#             agent=agent,
#         )

from textwrap import dedent
from crewai import Task
from tool import main, read_content, write_content, clean_html, clean_css

class ProjectTasks():
    def designer_task_html(self, agent, topic):
        return Task(
               description=f"""Generate a single HTML file containing mobile wireframes for a {topic} application.""",
               expected_output=f"""
                Create a well-structured HTML file with mobile wireframes for a {topic} application, adhering to the following specifications:

                1. Structure:
                - Create a `<body>` with at least six `<div class="mobile-frame">` elements.
                - Each `<div class="mobile-frame">` should represent a different screen relevant to the {topic} application.
                - Always include Register and Login screens.
                - The remaining screens should be specifically tailored to the {topic}.

                2. Content:
                - Register Screen: Include fields relevant to the {topic} (e.g., username, email, password, and any topic-specific fields).
                - Login Screen: Include standard login fields and any {topic}-specific login options.
                - Home Screen (Dashboard): 
                    * Display a summary or overview specifically relevant to the {topic}.
                    * Include quick action buttons or links to main features of the {topic} application.
                    * Ensure the design is attractive and user-friendly for the specify {topic} applications.
                - Additional Screens: Create at least seven more screens specific to the {topic} functionality.

                3. Navigation:
                - Use `<header>` for the top bar with screen titles.
                - Use `<main>` for the primary content area.
                - Include `<section>` tags to group related content within each screen.
                - Utilize form elements like `<input>`, `<button>`, and `<label>` where necessary.
                - Implement a consistent navigation menu (e.g., bottom tab bar or side menu).
                - Include icons for home, list view, profile, and other topic-specific sections.
                
                4. Style Link:
                - Include a `<link>` tag in the `<head>` section of the HTML file to link to the external CSS file: `<link rel="stylesheet" href="wireframe_css2.css">`.

                5. Class Names:
                - Use descriptive class names for elements that will be styled in the CSS.
                - Include classes like 'mobile-frame', 'nav-menu', 'button', 'input-field', etc.

                6. Comments:
                - Include detailed comments in the HTML explaining each section and any complex layout choices.
                - Add comments suggesting potential variations or additional features specific to the {topic}.

                The final output should be a single HTML file that, when opened in a browser and linked with the CSS file, displays a structured mobile wireframe for the {topic} application.
                """, 
                output_file="outs/wireframe_html4.html",
                tools = [main,read_content,write_content,clean_html],
                agent=agent,
        )
        
    def designer_task_css(self, agent, topic, context):
        return Task(
            description=f"""Generate a CSS file to style the HTML wireframes for a {topic} application.""",
            expected_output=f"""
                Create a CSS file to style the HTML wireframes for a {topic} application, adhering to the following specifications:

                1. **General Styling:**
                - Use `box-sizing: border-box;` globally.
                - Reset margin and padding for all elements.

                2. **Body:**
                - Set font family to Arial, sans-serif.
                - Center content using Flexbox.
                - Apply a light background color (#f4f4f4) and padding.

                3. **Mobile Frame:**
                    - Define `.mobile-frame` class with:
                    - Width: 360px
                    - Height: 640px
                    - Border: 1px solid #ccc
                    - Border-radius: 10px
                    - Box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)
                    - Background color: #fff
                    - Margin: 10px
                    - Padding: 20px
                    - Overflow-y: auto

                4. **Typography:**
                - Style headings (`h1`, `h2`, etc.) with bold font-weight and appropriate sizes.
                - Define styles for paragraphs with bottom margin.

                5. **Layout Styles:**
                - Style `header` with background color (#4CAF50), white text color, and centered text.
                - Style `main` and `section` with padding and background colors.

                6. **Navigation:**
                - Style `.nav-menu` fixed at the bottom with background color (#4CAF50).
                - Style navigation links with white text and hover effects.
                - Style `.sidebar` with smooth transitions.
                - Style `.menu-toggle` for sidebar toggling.

                7. **Buttons:**
                - Style `.button` with green background, white text, padding, and border-radius.

                8. **Form Elements:**
                - Style form elements with consistent padding, margin, and border.

                9. **Color Scheme:**
                - Define CSS variables for primary (#4CAF50) and secondary colors (#ccc).

                10. **Responsive Design:**
                - Add media queries for larger screens, adjusting `.mobile-frame` styles.

                11. **Comments:**
                - Include comments to explain styling choices and layout decisions.

                The final CSS file should link to the HTML and style the mobile wireframe for the {topic} application.
                """,
            output_file="outs/wireframe_css6.css",
            context=[context],
            tools=[main, read_content, write_content, clean_css],
            agent=agent,
        )

# from textwrap import dedent
# from crewai import Task

# class ProjectTasks():
#     def design_task(self, agent, topic):
#       return Task(
#         description=f"""Generate a single HTML file containing both the mobile wireframes and embedded CSS for a {topic} application. The output should not include any footer sections.""",
#         expected_output=f"""
#         Create a single HTML file that includes both the mobile wireframes and the CSS styling for a {topic} application. The file should exclude any footer sections.

#         1. **HTML Structure:**
#         - Include a `<style>` tag in the `<head>` section for the CSS.
#         - Create a `<body>` with at least six `<div class="mobile-frame">` elements.
#         - Each `<div class="mobile-frame">` should represent a different screen relevant to the {topic} application.
#         - Ensure to include Register and Login screens.
#         - Tailor the remaining screens to the specific functionality of the {topic}.
#         - **Do not include any footer sections.**

#         2. **HTML Content:**
#         - Register Screen: Include relevant fields (e.g., username, email, password, and any topic-specific fields).
#         - Login Screen: Include standard login fields and any {topic}-specific login options.
#         - Home Screen (Dashboard):
#             * Display an overview specific to the {topic}.
#             * Include action buttons or links to main features of the {topic} application.
#         - Additional Screens: Create at least seven more screens specific to {topic} functionality.
#         - **Ensure no footer section is present in any screen.**

#         3. **CSS Styling (Embedded in HTML):**
#         - **Mobile Frame Styling:**
#             - Set the width to 360px, height to 640px, apply border, rounded corners, and shadow.
#             - Use Flexbox to position the frames horizontally.
#         - **Layout Styles:**
#             - Implement a grid or flexbox layout for content.
#             - Style headers, main content areas, but omit any footer styling.
#         - **Navigation Styles:**
#             - Style `.nav-menu` with background color, text color, and layout.
#             - Include hover states for navigation links.
#         - **Button Styles:**
#             - Style `.button` with background color, text color, padding, border radius, and hover states.
#         - **Form Styles:**
#             - Style form elements for consistency and usability.
#         - **Layout:**
#             - Use Flexbox for horizontal positioning of the mobile frames.
#             - Implement a 4-point spacing system.
#         - **Typography:**
#             - Define font family and size, style headings and text elements.
#         - **Color Scheme:**
#             - Define a color scheme appropriate for the {topic}.
#             - Primary color is green, secondary color is gray.
#         - **Responsive Design:**
#             - Include media queries for basic responsiveness on larger screens.
#         - **Comments:**
#             - Include detailed comments in the CSS explaining styling choices.

#         The final output should be a single HTML file that, when opened in a browser, displays a well-styled mobile wireframe for the {topic} application without any footer sections.
#         """,
#         output_file="outs/wireframe_task.html",
#         agent=agent,
#     )


    # def design_task(self, agent, topic):
    #     return Task(
            # description=f"""Generate a single HTML file for a {topic} application wireframe. Focus on the core functionalities and interactive elements specific to the {topic}. Exclude headers, navigation, and footers. Ensure proper alignment of content using basic HTML and CSS. The wireframe should clearly show the application's features and layout.""",
            # expected_output=f"""
            # Create a single HTML file with a wireframe for a {topic} application. The wireframe should include:

            # 1. **Layout and Structure:**
            # - Focus on the main content and functionalities of the {topic} application.
            # - Do not include headers, navigation, or footers.
            # - Use containers and basic HTML elements to align and structure the content.

            # 2. **Interactive Elements:**
            # - **Buttons or Links:** Ensure these elements work and reveal or update content when clicked. Use simple JavaScript for interactivity.
            # - **Forms:** Include forms for user input and ensure they handle submissions.
            # - **Dynamic Elements:** Add features like charts or toggle panels, if relevant.

            # 3. **Data Display:**
            # - Use tables, lists, or cards to show information related to the {topic}.
            # - Add placeholder content for demonstration purposes.

            # 4. **Basic Styling:**
            # - Apply basic CSS for alignment and spacing:
            #   - Use `.container` to center content.
            #   - Apply margins and padding to align elements.

            # 5. **Single File Integration:**
            # - Include HTML, CSS, and JavaScript all in one file:
            #   - **HTML:** Structure the content.
            #   - **CSS:** Add basic styles within a `<style>` tag.
            #   - **JavaScript:** Add functionality within a `<script>` tag.

            # The final output should be a single HTML file that displays a clear and functional wireframe for a {topic} application, focusing on core features and proper alignment without headers, navigation, or footers.
            # """,
    #         output_file="outs/wireframe_task.html",
    #         tools=[clean_html],
    #         agent=agent,
    #     )
