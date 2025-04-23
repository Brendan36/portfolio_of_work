import streamlit as st
import base64


def show():
    from utils.toast_manager import handle_redirect_toast
    handle_redirect_toast()
    st.title("| be |  *©*")
    st.subheader("*uncover truth, ignite change*", divider='rainbow')

    # dyk1 = """
    #     A commercially packed 1.5kg chicken requires 5kg of feed.\n
    #     KFC's Thai restaurant chain serves approximately 800,000 pieces of fried chicken daily, or 292 million pieces per year
    #     (assuming 8pieces = 1 chicken) - That's equivalent to 100,000 chickens per day or 3,000,000 chickens per year. \n
    #     it takes 550,000kg of feed (550 ton) to produce the 100,000 (150 ton) chickens that are sold daily.\n
    #     \n
    #     Assuming 1 chicken = 2 kg live weight\n
    #     Which consumed 11 kg of feed (5.5kg of feed per 1 kg of gain for a typical broiler chicken).\n
    #     The end product is 1.5 kg of meat.\n
    #
    #     **Is this sustainable?**
    #
    #     """
    #
    # dyk2 = """
    #     To produce 1 kg of beef: 13–15 kg of feed (forage + grain) is required.\n
    #     15,000 liters of water (for feed production, drinking water, and processing).\n
    #     -> **! That's 15,000 liters of water for 1 kg of beef !** <- *Why support this?*🤔\n
    #
    #     FYI: These numbers are based on the Average Feed Requirements for rearing cattle:\n
    #
    #     We've assumed that 8 kg of feed per 1 kg of live weight gain for a typical beef cattle.
    #     Since only 60% of live weight translates to edible meat, the adjusted FCR is approximately:\n
    #     8kg feed / 0.6 (meat yield factor) = 13.33kg feed for 1kg beef.
    #     \n
    #     **Is this sustainable?**
    #     """
    #
    # col3, empty_col, col4 = st.columns([1.5, 0.1, 1.5])
    # with col3:
    #     st.subheader("Did You Know..?")
    #     st.info(dyk2)
    #
    # with col4:
    #     st.subheader("Did You Know..?")
    #     st.info(dyk1)
    #
    # st.header("*Food for Thought... IMO*", divider='rainbow')
    # st.write("*Most*.. commercial industries are not sustainable - Do you want to help us see past cute and often misleading labels?")
    # st.write("*People*.. should have access to alternative options - Do you intend to enable those options?")
    # st.write("*Are*.. we really doing the best we can? - Do you want to help us realise what we are doing?")
    # st.write(
    #     "*Ignorant*.. is what we are if, we blindly trust and support commercial industries (many of them only perpetuate the problems) - Do you want to finance the destruction of the planet?")
    # st.write("*To*.. become sustainable, we need to inspire others to take action through doing it ourselves - Do you want to maintain your blanket of cognitive ambivalence?")
    # st.write("*Change*.. is the only realistic option we have left - it's only too late when we're dead... - Do you want to wait?")
    # st.write("*In reality*.. we need to stop supporting industries that are intentionally misleading us - I want create and easier way to know that - Do you want to know?")
    #

    st.subheader("*what will you do?*", divider='rainbow')

    audio_file_path = "C:/Users/Dell/PycharmProjects/app2-portfolio/We Deserve To Dream.mp3"
    with open(audio_file_path, "rb") as f:
        audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()

    audio_player_base64 = f"""
        <audio autoplay loop controls>
            <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
        </audio>
    """
    st.markdown(audio_player_base64, unsafe_allow_html=True)
    st.write("*Artist: Xavier Rudd - We Deserve to Dream*")

    # ─── Footer ───
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    footer_html = """
        <p style="text-align:center; color:gray; font-size:0.8em; margin:0;">
          Built with 💡 by | be | © 2025
        </p>
        <p style="text-align:center; color:gray; font-size:0.8em; margin:0;">
         <a href="?page=about"     target="_self" style="color:gray; text-decoration:none;">| about</a> |
         <a href="?page=portfolio" target="_self" style="color:gray; text-decoration:none;">portfolio</a> |
         <a href="?page=contact"   target="_self" style="color:gray; text-decoration:none;">contact</a> | 
        </p>
        """
    col2.markdown(footer_html, unsafe_allow_html=True)