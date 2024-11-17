import React, { useState } from "react";
import styles from "./NotificationsPage.module.scss";

type Notification = {
    id: number;
    databaseId: string;
    coordinates: string;
    date: string;
    photo: string;
    status: string;
};

const notificationsData: Notification[] = [
    { id: 1, databaseId: "#12548796", coordinates: "8.741813 41.203591", date: "28 января, 12:30", photo: require("../RequestsPage/photo_2024-11-17_05-14-09.jpg"), status: "Требуется ручная проверка" },
    { id: 2, databaseId: "#12548796", coordinates: "6.45357 87.546464", date: "25 января, 10:40", photo: require("../RequestsPage/photo_2024-11-17_08-14-40.jpg"), status: "Обработаны ИИ" },
    { id: 3, databaseId: "#12548796", coordinates: "88.85675 76.7571", date: "20 января, 17:45", photo: require("../RequestsPage/photo_2024-11-17_05-14-09.jpg"), status: "Обработаны ИИ" },
    { id: 4, databaseId: "#12548796", coordinates: "12.4324 95.2348", date: "15 января, 03:29", photo: require("../RequestsPage/photo_2024-11-17_08-05-41.jpg"), status: "Требуется ручная проверка" },
    { id: 5, databaseId: "#12548796", coordinates: "32.4114 11.2948", date: "14 января, 20:40", photo: require("../RequestsPage/photo_2024-11-17_05-59-17.jpg"), status: "На фото нет баков" },
    { id: 6, databaseId: "#12548796", coordinates: "41.203591 8.741813", date: "25 января, 10:40", photo: require("../RequestsPage/photo_2024-11-17_05-14-27.jpg"), status: "Требуется ручная проверка" },
];

const NotificationsPage: React.FC = () => {
    const [filter, setFilter] = useState<string>("Все");

    const handleFilterChange = (newFilter: string) => {
        setFilter(newFilter);
    };

    const filteredNotifications = filter === "Все"
        ? notificationsData
        : notificationsData.filter((notification) => notification.status === filter);

    return (
        <div className={styles.notificationsPage}>
            <div className={styles.header}>
                <h1>Уведомления</h1>
                <div className={styles.filters}>
                    <button
                        className={filter === "Все" ? styles.activeFilter : ""}
                        onClick={() => handleFilterChange("Все")}
                    >
                        Все
                    </button>
                    <button
                        className={filter === "Обработаны ИИ" ? styles.activeFilter : ""}
                        onClick={() => handleFilterChange("Обработаны ИИ")}
                    >
                        Обработаны ИИ
                    </button>
                    <button
                        className={filter === "Требуется ручная проверка" ? styles.activeFilter : ""}
                        onClick={() => handleFilterChange("Требуется ручная проверка")}
                    >
                        Требуется ручная проверка
                    </button>
                </div>
            </div>
            <table className={styles.table}>
                <thead>
                <tr>
                    <th>ID в базе</th>
                    <th>Координаты</th>
                    <th>Дата</th>
                    <th>Фото</th>
                    <th>Статус</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {filteredNotifications.map((notification) => (
                    <tr key={notification.id}>
                        <td>{notification.databaseId}</td>
                        <td>{notification.coordinates}</td>
                        <td>{notification.date}</td>
                        <td>
                            <img src={notification.photo} alt="Фото" className={styles.photo} />
                        </td>
                        <td>
                                <span
                                    className={
                                        notification.status === "Обработаны ИИ"
                                            ? styles.processedStatus
                                            : notification.status === "Требуется ручная проверка"
                                                ? styles.manualCheckStatus
                                                : styles.defaultStatus
                                    }
                                >
                                    {notification.status}
                                </span>
                        </td>
                        <td>
                            <button className={styles.actionButton}>Отметить как "Решено"</button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
            <div className={styles.footer}>
            </div>
        </div>
    );
};

export default NotificationsPage;
