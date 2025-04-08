import streamlit as st

st.title("Đăng ký tài khoản")

progress = st.progress(0)

username = st.text_input("Tài khoản")
password = st.text_input("Mật khẩu", type="password")
re_password = st.text_input("Nhập lại mật khẩu", type="password")
fullname = st.text_input("Tên người dùng")
email = st.text_input("Email")

filled_fields = 0
total_fields = 5

if username != "":
    filled_fields += 1
if password != "":
    filled_fields += 1
if re_password != "":
    filled_fields += 1
if fullname != "":
    filled_fields += 1
if email != "":
    filled_fields += 1

if st.button("Đăng ký"):
    if filled_fields < total_fields:
        progress.progress(int(filled_fields / total_fields * 100))
        st.write("Bạn chưa điền đầy đủ thông tin.")
    elif password != re_password:
        st.write("Mật khẩu nhập lại không khớp.")
    else:
        progress.progress(100)
        st.write("Đăng ký thành công!")
        st.write("Thông tin bạn đã nhập:")
        st.write("Tài khoản:", username)
        st.write("Tên người dùng:", fullname)
        st.write("Email:", email)
