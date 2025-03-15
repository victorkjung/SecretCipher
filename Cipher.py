import streamlit as st

def caesar_encode(message: str, shift: int) -> str:
    """
    Encode a message using the Caesar Cipher.

    Parameters:
        message (str): The message to encode.
        shift (int): The shift number to use for encoding.

    Returns:
        str: The encoded message.
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Only shift letters
            shift_amount = shift % 26  # Handle shifts larger than 26
            base = ord('a') if char.islower() else ord('A')
            encoded_message += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            encoded_message += char  # Keep non-alphabetic characters as-is
    return encoded_message

def caesar_decode(message: str, shift: int) -> str:
    """
    Decode a message encoded with the Caesar Cipher.

    Parameters:
        message (str): The encoded message.
        shift (int): The shift number that was used for encoding.

    Returns:
        str: The decoded message.
    """
    return caesar_encode(message, -shift)

def main():
    st.title("🐰 Cipher Messenger Center")
    st.write("Welcome to the 🥷 communication app! 🕵️‍♂️")
    
    # Input for shift number
    shift = st.number_input("Enter the shift number (keep it secret!):", value=3, step=1)
    
    # Tabs for encoding and decoding
    tab1, tab2 = st.tabs(["Encode Message", "Decode Message"])
    
    # Encoding tab
    with tab1:
        st.header("Encode a Message")
        message_to_encode = st.text_area("Enter your message to encode:")
        if st.button("Encode", key="encode_button"):
            if message_to_encode:
                encoded_message = caesar_encode(message_to_encode, shift)
                st.success("Encoded Message:")
                st.code(encoded_message)
            else:
                st.error("Please enter 👩‍💻 a message to ✅ encode :")
    
    # Decoding tab
    with tab2:
        st.header("Decode a Message")
        message_to_decode = st.text_area("Enter your message to 🌐 decode ⛳ :")
        if st.button("Decode", key="decode_button"):
            if message_to_decode:
                decoded_message = caesar_decode(message_to_decode, shift)
                st.success("Decoded Message:")
                st.code(decoded_message)
            else:
                st.error("Please enter a message to decode.")
    
    # Sidebar instructions
    st.sidebar.header("How to use Messenger App")
    st.sidebar.write("1. Agree on a shift number with your friend (e.g., 3).")
    st.sidebar.write("2. Use the 'Encode Message' tab to encode your message.")
    st.sidebar.write("3. Share the encoded message with your friend.")
    st.sidebar.write("4. Use the 'Decode Message' tab to decode your friend's message.")
    st.sidebar.write("5. Keep the shift number secret! 🤫")

if __name__ == "__main__":
    main()
