import numpy as np
import pyvista as pv

# ── 1. 파라미터 (모두 m 단위) ────────────────────────────────────────────
board_len = 0.10  # 플레어 길이  L  (y축)  ≈ 100 mm
board_wid = 0.06  # 기판 폭     W  (x축)  ≈ 60 mm
board_thk = 0.0016  # FR‑4 두께   t  (z축)  ≈ 1.6 mm

slot_gap = 0.003  # 피드 갭(초기 슬롯 폭)    ≈ 3 mm
slot_mouth = 0.050  # 슬롯 말단 폭               ≈ 50 mm
n_curve_pts = 200  # 지수 플레어 곡선 해상도

sma_len = 0.012  # SMA inner pin 길이
sma_rad = 0.001  # SMA inner pin 반경


# ─────────────────────────────────────────────────────────────────────────

def make_vivaldi_board():
    """PCB 솔리드 + 슬롯 곡선을 반환한다."""
    # 1) 기판(직육면체)
    board = pv.Box(bounds=(-board_wid / 2, board_wid / 2,
                           0, board_len,
                           -board_thk / 2, board_thk / 2))

    # 2) 지수 플레어 슬롯(라인) – 시각화 전용
    k = np.log(slot_mouth / slot_gap) / board_len
    y = np.linspace(0, board_len, n_curve_pts)
    half = 0.5 * slot_gap * np.exp(k * y)  # y별 반폭
    ptsU = np.c_[half, y, np.zeros_like(y)]  # 상단 곡선
    ptsL = np.c_[-half, y, np.zeros_like(y)]  # 하단 곡선
    return board, pv.Spline(ptsU), pv.Spline(ptsL)


# ── 2. 두 장의 직교 PCB 생성 ─────────────────────────────────────────────
# (a) 수평편파판: 기본 보드를 z축 +90° 회전 → x=0 평면
h_board, hU, hL = make_vivaldi_board()
h_board.rotate_y(90, inplace=True)
hU.rotate_y(90, inplace=True)
hL.rotate_y(90, inplace=True)
#h_board.rotate_z(90, inplace=True)
#hU.rotate_z(90, inplace=True);
#hL.rotate_z(90, inplace=True)

# (b) 수직편파판: 그대로 사용
v_board, vU, vL = make_vivaldi_board()

# ── 3. SMA 피드(단순 원기둥) ─────────────────────────────────────────────
sma = pv.Cylinder(center=(0, 0, 0), direction=(0, 0, 1),
                  radius=sma_rad, height=sma_len)

# ── 4. 렌더링 ───────────────────────────────────────────────────────────
pl = pv.Plotter()
pl.add_mesh(v_board, color="#ff7f0e", opacity=0.60, show_edges=True)  # vertical board
pl.add_mesh(h_board, color="#1f77b4", opacity=0.60, show_edges=True)  # horizontal board
for ln in (vU, vL, hU, hL):  # slot edges
    pl.add_mesh(ln, color="black", line_width=2)
pl.add_mesh(sma, color="gold", smooth_shading=True)  # SMA pin

pl.show_axes()
pl.set_background("white")
pl.show()
