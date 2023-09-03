import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def quad_plot(a, b, c):
    x = np.linspace(-10,10)
    y = a * x ** 2 + b * x + c

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_xlabel('f(x)')
    ax.set_title(f"qudratic equation : {a}x^2 + {b}x + {c}")

    st.pyplot(fig)

def main():

    st.title("Math Visualization : Quadratic Equation")
    st.sidebar.header("Quadratic Equation Co-Effficients")
    a = st.sidebar.slider("co-efficient a",-10,10,0)
    b = st.sidebar.slider("co-efficient b",-10,10,0)
    c = st.sidebar.slider("co-efficient c",-10,10,0)
    quad_plot(a,b,c)
if __name__=="__main__":
    main()