import cv2
import matplotlib.pyplot as plt
from flask import Flask, render_template
import mpld3
app = Flask(__name__)

@app.route('/')
def index():
    img = cv2.imread('static/sample.png')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_value = 128
    max_value = 255
    threshold_type = cv2.THRESH_BINARY
    _, binary_img = cv2.threshold(gray_img, threshold_value, max_value, threshold_type)
    fig, axs = plt.subplots(1, 3, figsize=(5,2))
    axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[1].imshow(gray_img, cmap='gray')
    axs[2].imshow(binary_img)
    graph_html = mpld3.fig_to_html(fig)
    return render_template('index.html',graph_html=graph_html)

if __name__ == '__main__':
    app.run()



