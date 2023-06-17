import streamlit as st

def style():
    st.set_page_config(page_title="Pricing", page_icon="https://github.com/AnasMations/StudySync/blob/36ae1cad78544b8a07239d1cefa141a59f6305c8/img/icon.png?raw=true")
    st.markdown(
        """
        <style>
            
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(220deg, #fbeaf7,#ffffff, #dfeefb);
                color: black;
            }
            

        div.stButton > button:first-child {
            font-size: 24px;
            padding: 16px 32px;
            background-color: #FFFFFF;
            color: #262730;
            border: none;
            display: block;
            margin-left: auto;
            margin-right:auto;
            border-radius: 12px; /* Add rounded edges */
            box-shadow: 0 0px 15px rgba(0, 0, 0, 0.2); /* Add shadow for a 3D look */
            transition: all 0.3s ease-in-out; /* Add smooth transition for hover effects */
        
        }

        div.stButton > button:first-child:hover {
            cursor: pointer;
            border: none;
            background-color: #6ebabf;
            transform: translateY(-5px) scale(1.02); /* Animate movement upwards and scale */
            box-shadow: 0 10px 40px rgba(110, 186, 191, 1); /* Enlarge shadow on hover for a 3D effect */
        
        }
        
        @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def about_section():
    st.title("Pricing Plans")

    with st.container():
        col1, col2, col3 = st.columns(3)

        # Plan 1
        with col1:
            st.write('''                                
              <style>
                .box {
                  border: 1px solid #cccccc;
                  background-color: #dfeefb;
                  padding: 15px;
                  border-radius: 5px;
                  box-shadow: 0 0px 15px rgba(0, 0, 0, 0.1);
                  transition: all 0.3s ease-in-out;
                }
                .box:hover {
                  cursor: pointer;
                  border: 1px solid #cccccc;
                  background-color: #dfeefb;
                  padding: 15px;
                  border-radius: 5px;
                  box-shadow: 0 10px 40px rgba(110, 186, 191, 0.9);
                }
                .title {
                  font-size: 24px;
                  font-weight: normal;
                }
                .price {
                  font-size: 44px;
                  font-weight: bold;
                  color: black;
                }
                .description {
                  color: gray;
                }
              </style>

              <div class="box">
                  <p class="title">Free</p>
                  <p class="price">$0.00</p>
                  <p></p>
                  <p>⏳ 1 Month Trial</p>
                  <p>🔴 Daily Limited Usage</p>
                  <p>🔴 Max Tokens 150</p>
                  <p>✅ Topic Summaries</p>
                  <p>✅ Multiple Choices</p>
                  <p>❌ Flash Cards</p>
                  <p>❌ Video Summaries</p>
                  <p>❌ PDF Summaries</p>
                  <p>❌ Mind Maps</p>
                  <p>❌ Remove Ads</p>
                  <p>❌ 24/7 Support</p>
                  <hr>
                  <p class="description">Enjoy a free version</p>
              </div>
            ''', unsafe_allow_html=True)

        # Plan 2
        with col2:
            st.write('''
              <div class="box">
                  <p class="title">Premium</p>
                  <p class="price">$14.99</p>
                  <p>⏳ 1 Month Access</p>
                  <p>🟢 Unlimited Usage</p>
                  <p>🟢 Max Tokens 2000</p>
                  <p>✅ Topic Summaries</p>
                  <p>✅ Multiple Choices</p>
                  <p>✅ Flash Cards</p>
                  <p>✅ Video Summaries</p>
                  <p>✅ PDF Summaries</p>
                  <p>✅ Mind Maps</p>
                  <p>✅ Remove Ads</p>
                  <p>❌ 24/7 Support</p>
                  <hr>
                  <p class="description">Great for students</p>
              </div>
            ''', unsafe_allow_html=True)

        # Plan 3
        with col3:
            st.write('''
              <div class="box">
                  <p class="title">Enterprise</p>
                  <p class="price">Contact</p>
                  <p>🟢 Get all features from premium integrated for your Organization</p>
                  <p>✅ 24/7 Support</p>
                  <p>✅ Dedicated Account Manager</p>
                  <hr>
                  <p class="description">Perfect for large organizations such as Schools and Universities</p>
              </div>
            ''', unsafe_allow_html=True)

# Example usage
style()
about_section()
