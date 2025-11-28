"""from moviepy.editor import VideoFileClip, vfx

# 비디오 파일 불러오기
input_video_path = "./videos/a.mp4"
output_video_path = "./videos/b.mp4"

# VideoFileClip 객체로 비디오 로드
clip = VideoFileClip(input_video_path)

# 영상 속도 두 배로 만들기 (시간을 절반으로)
fast_clip = clip.fx(vfx.speedx, 2)

# 출력 파일로 저장
fast_clip.write_videofile(output_video_path, codec="libx264")"""

import cv2

# 비디오 파일 경로
input_video_path = "./videos/a.mp4"
output_video_path = "./videos/b.mp4"

# 비디오 읽기
cap = cv2.VideoCapture(input_video_path)

# 비디오 속성 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)  # 원본 비디오 FPS
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 속도 두 배로 만들기 위해 FPS 변경
new_fps = fps * 0.2

# 비디오 작성 객체
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video_path, fourcc, new_fps, (width, height))

# 비디오 프레임을 읽고 처리하기
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)  # 프레임을 출력 파일에 저장

# 자원 해제
cap.release()
out.release()

print(f"Video saved as {output_video_path}")
