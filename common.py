RC9_PROJ_PATH = "RCPJ=C:\\Users\\ijiwa\\Documents\\WINCAPSIII\\VS050_RC9\\VS050_RC9\\default.rcpj"
POSITION = [0.0, -329.02, 260.0, -180.0, 0.0, 118.61]
FIG = -1

def convert_posedata(pos, fig=FIG):
    pos_str = ",".join(map(str, pos))
    return f"P({pos_str},{fig})"
