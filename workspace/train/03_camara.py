import os

from ultralytics import YOLO
import cv2

ubicacion = os.path.dirname(os.path.abspath(__file__))

# Define la ruta del modelo entrenado
model_path = os.path.join(ubicacion, "guns.pt")

# Carga el modelo personalizado
model = YOLO(model_path)  # Carga un modelo personalizado

# Configura el umbral de confianza
threshold = 0.5

# Inicia la captura de video desde la cámara web
cap = cv2.VideoCapture(0)  # 0 generalmente representa la primera cámara web disponible

# Obtiene las propiedades del video de la cámara web para configurar el grabador de video
ret, frame = cap.read()
if not ret:
    print("Error: no se pudo obtener un marco de la cámara web.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

H, W, _ = frame.shape
video_path_out = "webcam_output.mp4"
out = cv2.VideoWriter(
    video_path_out,
    cv2.VideoWriter_fourcc(*"MP4V"),
    int(cap.get(cv2.CAP_PROP_FPS)),
    (W, H),
)

while ret:
    # Realiza la detección en el marco actual
    results = model(frame)[0]

    # Dibuja los resultados de la detección
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(
                frame,
                results.names[int(class_id)].upper(),
                (int(x1), int(y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.3,
                (0, 255, 0),
                3,
                cv2.LINE_AA,
            )

    # Muestra el marco en una ventana
    cv2.imshow("Frame", frame)

    # Escribe el marco procesado en el archivo de salida
    out.write(frame)

    # Lee el siguiente marco de la cámara web
    ret, frame = cap.read()

    # Espera la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libera el objeto de captura y cierra todas las ventanas
cap.release()
out.release()
cv2.destroyAllWindows()
