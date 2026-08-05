import cv2

# 1. Načtení vestavěného kaskádového klasifikátoru pro obličej
face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

# 2. Spuštění video streamu z webkamery (0 je index výchozí kamery)
cap = cv2.VideoCapture(0)

print("Stiskněte 'q' pro ukončení programu.")

while True:
    # Zachycení aktuálního snímku z kamery
    ret, frame = cap.read()
    if not ret:
        break

    # Zobrazení výsledného obrazu v okně
    cv2.imshow('Kamera', frame)

# Uvolnění kamery a zavření oken
cap.release()
cv2.destroyAllWindows()
