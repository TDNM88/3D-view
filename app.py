import gradio as gr

def view_3d_model(file_path):
    return file_path

demo = gr.Interface(
    fn=view_3d_model,
    inputs=gr.inputs.File(type="file", label="Upload your 3D model file (OBJ, GLB, or GLTF formats)"),
    outputs=gr.outputs.Model3D(clear_color=[0.0, 0.0, 0.0, 0.0], label="3D Model Viewer"),
    title="3D Asset Viewer",
    description="Upload a 3D model file to view it in the viewer below."
)

if __name__ == "__main__":
    demo.launch()
