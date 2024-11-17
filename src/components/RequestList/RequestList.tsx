import React, { useState } from "react";
import styles from "./RequestList.module.scss";

type TransformedRequest = {
    id: number;
    username: string;
    type: string;
    coordinates: string;
    date: string;
    photo: string;
    status: string;
};

type RequestListProps = {
    requests: TransformedRequest[];
    onSelectRequest: (id: number) => void;
};

const RequestList: React.FC<RequestListProps> = ({ requests, onSelectRequest }) => {
    const [filter, setFilter] = useState<string>("all");

    const filteredRequests = requests.filter((request) => {
        if (filter === "all") return true;
        return request.status === filter;
    });

    const handleFilterChange = (newFilter: string) => {
        setFilter(newFilter);
    };

    return (
        <div className={styles.requestList}>
            <div className={styles.filters}>
                <button
                    className={filter === "all" ? styles.activeFilter : ""}
                    onClick={() => handleFilterChange("all")}
                >
                    Все заявки
                </button>
                <button
                    className={filter === "Рассматривается" ? styles.activeFilter : ""}
                    onClick={() => handleFilterChange("Рассматривается")}
                >
                    Рассматривается
                </button>
                <button
                    className={filter === "Выполнено" ? styles.activeFilter : ""}
                    onClick={() => handleFilterChange("Выполнено")}
                >
                    Выполнено
                </button>
            </div>
            <table className={styles.table}>
                <thead>
                <tr>
                    <th>Отправитель</th>
                    <th>ID</th>
                    <th>Тип</th>
                    <th>Координаты</th>
                    <th>Дата</th>
                    <th>Фото</th>
                    <th>Статус</th>
                </tr>
                </thead>
                <tbody>
                {filteredRequests.length > 0 ? (
                    filteredRequests.map((request) => (
                        <tr key={request.id} onClick={() => onSelectRequest(request.id)}>
                            <td>{request.username}</td>
                            <td>#{request.id}</td>
                            <td>{request.type}</td>
                            <td>{request.coordinates}</td>
                            <td>{request.date}</td>
                            <td>
                                <img
                                    src={request.photo}
                                    alt="Фото заявки"
                                    className={styles.photo}
                                />
                            </td>
                            <td>
                                <button
                                    className={
                                        request.status === "Выполнено"
                                            ? styles.completedStatus
                                            : styles.inProgressStatus
                                    }
                                >
                                    {request.status}
                                </button>
                            </td>
                        </tr>
                    ))
                ) : (
                    <tr>
                        <td colSpan={7} className={styles.noData}>
                            Нет заявок для отображения
                        </td>
                    </tr>
                )}
                </tbody>
            </table>
        </div>
    );
};

export default RequestList;
