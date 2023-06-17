import streamlit as st

def about_section():
    st.set_page_config(page_title="About", page_icon="img\icon.png")
    st.markdown(
        """
        <div style="background-color:#f9f9f9;padding:20px;border-radius:10px;">
            <h1 style="text-align:center;color:#333;">Welcome to Our Awesome App!</h1>
            <p style="text-align:center;font-size:18px;color:#666;">
                We are a team of 3 passionate individuals dedicated to creating amazing software.
                Our goal is to provide innovative solutions to everyday problems and deliver
                exceptional user experiences.
            </p>
            <div style="display:flex;justify-content:center;margin-top:30px;">
                <img src="https://github.com/AnasMations/StudySync/blob/main/img/Study%20Sync.png?raw=true" alt="Logo" width="300" style="border-radius:10px;">
            </div>
            <h2 style="text-align:center;color:#333;margin-top:40px;">Meet the Team</h2>
            <div style="display:flex;justify-content:center;margin-top:30px;">
                <div style="text-align:center;margin-right:40px;">
                    <img src="https://scontent.fcai19-6.fna.fbcdn.net/v/t39.30808-6/307515015_2657884574342657_6966984511757276880_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=174925&_nc_ohc=BMbSG5el4UMAX9PWN46&_nc_ht=scontent.fcai19-6.fna&oh=00_AfBU7GJGNrTU8y-w7RzeC_mx5uH7XVMxdH1q3o6DL8q_jg&oe=649198C0" alt="Eslam Mohamed" width="150" height="150" style="border-radius:50%;">
                    <h3 style="color:#333;margin-top:10px;">Eslam Mohamed</h3>
                    <p style="color:#666;">Data Scientist</p>
                    <div>
                        <a href="https://www.linkedin.com/in/eslam-ahmed-249730194/" target="_blank">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/800px-LinkedIn_icon_circle.svg.png" alt="LinkedIn" width="30" height="30">
                        </a>
                        <a href="https://github.com/Eslam21" target="_blank">
                            <img src="https://static.vecteezy.com/system/resources/thumbnails/016/833/872/small/github-logo-git-hub-icon-on-white-background-free-vector.jpg" alt="GitHub" width="30" height="30" style="margin-left:10px;">
                        </a>
                    </div>
                </div>
                <div style="text-align:center;margin-right:40px;">
                    <img src="https://avatars.githubusercontent.com/u/72975894?v=4" alt="Mariam Barakat" width="150" height="150" style="border-radius:50%;">
                    <h3 style="color:#333;margin-top:10px;">Mariam Barakat</h3>
                    <p style="color:#666;">Data Scientist</p>
                    <div>
                        <a href="https://www.linkedin.com/in/mariam-barakat/" target="_blank">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/800px-LinkedIn_icon_circle.svg.png" alt="LinkedIn" width="30" height="30">
                        </a>
                        <a href="https://github.com/Myriam2002" target="_blank">
                            <img src="https://static.vecteezy.com/system/resources/thumbnails/016/833/872/small/github-logo-git-hub-icon-on-white-background-free-vector.jpg" alt="GitHub" width="30" height="30" style="margin-left:10px;">
                        </a>
                    </div>
                </div>
                <div style="text-align:center;">
                    <img src="https://avatars.githubusercontent.com/u/21877450?v=4" alt="Anas Ahmed" width="150" height="150" style="border-radius:50%;">
                    <h3 style="color:#333;margin-top:10px;">Anas Ahmed</h3>
                    <p style="color:#666;">Software Engineer</p>
                    <div>
                        <a href="https://www.linkedin.com/in/anas-ahmed-hassan/" target="_blank">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/LinkedIn_icon_circle.svg/800px-LinkedIn_icon_circle.svg.png" alt="LinkedIn" width="30" height="30">
                        </a>
                        <a href="https://github.com/AnasMations" target="_blank">
                            <img src="https://static.vecteezy.com/system/resources/thumbnails/016/833/872/small/github-logo-git-hub-icon-on-white-background-free-vector.jpg" alt="GitHub" width="30" height="30" style="margin-left:10px;">
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Example usage
about_section()
