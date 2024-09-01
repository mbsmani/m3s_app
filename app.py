import streamlit as st
st.set_page_config(page_title="M3S Traders", page_icon=":office:", layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stHeader"],
    [data-testid="stAppViewContainer"] {
        background-color: #c9dcd3;
        color: #205355
    }
    [data-testid="column"] img {
        margin-top: 17.5px
    }
    [data-testid="stMarkdownContainer"],
    [data-testid="StyledLinkIconContainer"]{
        color: #205355
    }
    .st-cq{
        background-color: #a9a97f
    }
    [data-testid="stForm"]{
        border: 1px solid #a9a97f
    }
    .header {
        display: flex;
        align-items: center;
        padding: 10px 0;
    }
    .header img {
        width: 50px;  /* Adjust the logo size */
        margin-right: 20px;
    }
    .header h1 {
        font-size: 2.5em;  /* Adjust the title size */
        margin: 0;
    }
    .service-card {
        background-color: #205355;
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
        width: 30%;
        display: inline-block;
        vertical-align: top;
        color: #fec76f;
    }
    .service-card h3 {
        margin-top: 0;
        font-size: 1.5em;
        color: #a9a97f;
    }
    h3 [data-testid="StyledLinkIconContainer"] {
        color: #a9a97f
    }
    .service-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-evenly;
    }
    .process-container {
        margin-top: 40px;
        position: relative;
        padding-left: 40px;
    }
    .process-step {
        display: flex;
        margin-bottom: 30px;
        align-items: center;
        position: relative;
    }
    .process-step::before {
        content: "";
        position: absolute;
        left: 20px;
        top: 0;
        bottom: 0;
        width: 2px;
        background-color: #fec76f;
    }
    .step-number {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #205355;
        color: #fec76f;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5em;
        font-weight: bold;
        margin-right: 20px;
        position: relative;
        z-index: 1;
    }
    .step-content h3 {
        margin: 0;
        font-size: 1.5em;
        color: #205355;
    }
    .step-content h3 [data-testid="StyledLinkIconContainer"] {
        color: #205355;
    }
    .step-content p {
        margin: 5px 0 0 0;
        color: #205355;
    }
    .process-step:last-child::before {
        height: 50%;
    }
    hr {
        border-bottom: 1px solid #a9a97f
    }
    </style>
    """,
    unsafe_allow_html=True,
)

cols = st.columns([0.12,2])
with cols[0]:
    st.image('assets/logo_m3s.jpg',width=65)
with cols[1]:
    st.markdown(
        f"""
        <div class="header">
            <h1>M3S TRADERS</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

tabs = st.tabs(["Home", "Products", "Contact"])

with tabs[0]:
    st.title("Welcome to M3S Traders")
    st.write("""Welcome to M3S Traders Private Limited, a newly established cashew nut
             processing company, founded on April 16, 2024. We are committed to
             providing high-quality, flavorful cashew nuts that cater to diverse taste preferences.
    """)

    st.title("About Us")
    st.write("""
    **Founded on April 16, 2024, M3S Traders Private Limited is an innovative and forward-thinking 
    enterprise committed to sourcing and delivering the finest cashews from around the world to markets 
    that value premium quality and excellence. As a newly established company with a visionary approach,
    we are dedicated to providing exceptional cashews while adhering to sustainable practices and fostering
    strong relationships with both our suppliers and customers.**
    """)

    st.markdown(
        """
        <div class="service-container" style="text-align: center">
            <div class="service-card">
                <h3>Mission</h3>
                <p>To deliver high-quality cashew products with a focus on customer satisfaction</p>
            </div>
            <div class="service-card">
                <h3>Vision</h3>
                <p>To be a leader in the industry, known for innovation and excellence.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h2 style='text-align: center; color: #c9dcd3;'>Empowering Women Through Employment</h2>
        <div class="service-container">
            <div class="service-card">
                <h3>Creating Opportunities</h3>
                <p>We provide direct employment opportunities for women in our cashew processing facility, 
                empowering them to achieve financial independence and improve their lives.</p>
            </div>
            <div class="service-card">
                <h3>Skills Development</h3>
                <p>We invest in training programs to enhance the skills and knowledge of our female employees, 
                equipping them for a brighter future.</p>
            </div>
            <div class="service-card">
                <h3>Economic Empowerment</h3>
                <p>Our commitment to women's empowerment contributes to the economic development of local communities, 
                creating a positive ripple effect.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h2 style='text-align: center; color: #c9dcd3;'>Commitment to Sustainable Practices</h2>
        <div class="service-container">
            <div class="service-card">
                <h3>Sustainable Sourcing</h3>
                <p>We source our cashews from ethical and sustainable farms, ensuring responsible agricultural practices.</p>
            </div>
            <div class="service-card">
                <h3>Environmental Responsibility</h3>
                <p>We minimize our environmental impact by implementing energyefficient processes and reducing waste.</p>
            </div>
            <div class="service-card">
                <h3>Community Engagement</h3>
                <p>We actively engage with local communities, promoting sustainable development and environmental awareness.</p>
            </div>
            <div class="service-card">
                <h3>Ethical Production</h3>
                <p>We are committed to fair labor practices and ethical sourcing throughout our supply chain.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with tabs[1]:
    st.header("Our Cashew Nut Product Line")
    st.markdown(
        """
        <div class="service-container">
            <div class="service-card">
                <h3>Plain</h3>
                <p>Hand graded premium cashews</p>
            </div>
            <div class="service-card">
                <h3>Roasted/Salted</h3>
                <p>Premium cashews roasted to perfection either directly or salted.</p>
            </div>
            <div class="service-card">
                <h3>Cinnamon Sugar</h3>
                <p>A sweet and warm treat, perfect for a comforting snack or dessert topping.</p>
            </div>
            <div class="service-card">
                <h3>Spicy Chili</h3>
                <p>A fiery kick for spice lovers, with a perfect balance of heat and nuttiness.</p>
            </div>
            <div class="service-card">
                <h3>Salt and Pepper</h3>
                <p>A classic combination, delivering a savory and crunchy delight.</p>
            </div>
            <div class="service-card">
                <h3>Caramelized</h3>
                <p>A decadent and indulgent flavor, with a rich caramel glaze.</p>
            </div>
            <div class="service-card">
                <h3>Chocolate Covered</h3>
                <p>A luxurious combination, featuring premium chocolate and premium cashews.</p>
            </div>
            <div class="service-card">
                <h3>BBQ</h3>
                <p>A smoky and savory flavor, reminiscent of classic barbecue flavors.</p>
            </div>
            <div class="service-card">
                <h3>Tandoori</h3>
                <p>A vibrant and aromatic flavor, inspired by traditional Indian cuisine.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h2 style='text-align: center; color: #ffd700;'>Our Manufacturing Process</h2>
        <div class="process-container">
            <div class="process-step">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h3>Raw Cashew Arrival</h3>
                    <p>We receive high-quality raw cashews from our trusted suppliers.</p>
                </div>
            </div>
            <div class="process-step">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h3>Quality Control</h3>
                    <p>Thorough quality checks are conducted to ensure the best quality cashews.</p>
                </div>
            </div>
            <div class="process-step">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h3>Roasting and Flavoring</h3>
                    <p>The cashews are roasted to perfection and seasoned with our unique flavor blends.</p>
                </div>
            </div>
            <div class="process-step">
                <div class="step-number">4</div>
                <div class="step-content">
                    <h3>Packaging and Distribution</h3>
                    <p>The finished product is carefully packaged and distributed to our valued customers.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with tabs[2]:
    st.title("Contact Us")
    st.write("We would love to hear from you. Please fill out the form below or reach out to us directly.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.write(f"Thank you, {name}. We have received your message and will get back to you at {email}.")


st.markdown("<br><hr><center>© 2024 M3S Traders. All rights reserved.</center>", unsafe_allow_html=True)
