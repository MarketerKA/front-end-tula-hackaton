import React from "react";
import styles from "./RequestDetails.module.scss";

type RequestDetailsProps = {
    request: {
        id: number;
        username: string; // Заменено с sender на username
        type: string;
        coordinates: string; // Заменено с address на coordinates
        date: string;
        status: string;
        photo: string;
        description: string;
    };
};

const translateStatus = (status: string): string => {
    switch (status) {
        case "in_progress":
            return "Рассматривается";
        case "completed":
            return "Выполнено";
        default:
            return status;
    }
};

const translateType = (type: string): string => {
    switch (type) {
        case "dirt":
            return "Свалка";
        default:
            return "Не убрано";
    }
};

const RequestDetails: React.FC<RequestDetailsProps> = ({request}) => {
    return (
        <div className={styles.requestDetails}>
            <h2>Заявка #{request.id}</h2> {/* Используем id вместо requestId */}
            <div className={styles.detailsContainer}>
                <div className={styles.detailsRow}>
                    <div className={styles.columnName}>Отправитель</div>
                    <div className={styles.columnValue}>{request.username}</div>
                </div>
                <div className={styles.detailsRow}>
                    <div className={styles.columnName}>ID</div>
                    <div className={styles.columnValue}>#{request.id}</div>
                </div>
                <div className={styles.detailsRow}>
                    <div className={styles.columnName}>Тип</div>
                    <div className={styles.columnValue}>{translateType(request.type)}</div>
                </div>
                <div className={styles.detailsRow}>
                    <div className={styles.columnName}>Координаты</div>
                    <div className={styles.columnValue}>{request.coordinates}</div>
                </div>
                <div className={styles.detailsRow}>
                    <div className={styles.columnName}>Дата</div>
                    <div className={styles.columnValue}>{request.date}</div>
                </div>
                <div className={styles.detailsRow}>
                    <div className={styles.columnName}>Статус</div>
                    <div className={styles.columnValue}>
      <span
          className={`${styles.status} ${
              request.status === "completed" ? styles.completed : styles.inProgress
          }`}
      >
        {translateStatus(request.status)}
      </span>
                    </div>
                </div>
                <div className={styles.photos}>
                    <img src={request.photo} alt="Фото заявки"/>
                </div>

            </div>
            <div className={styles.description}>
                <p>{request.description}</p>
            </div>
            <div className={styles.actions}>
                <button>Назначить ответственное лицо</button>
                <button>Хартия</button>
                <button>Еще кто-то</button>
                <button>Подтвердить</button>
            </div>
        </div>
    );
};

export default RequestDetails;
