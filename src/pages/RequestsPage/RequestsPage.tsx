import React, { useState, useEffect } from "react";
import RequestList from "../../components/RequestList/RequestList";
import RequestDetails from "../../components/RequestDetails/RequestDetails";
import styles from "./RequestsPage.module.scss";


const ITEMS_PER_PAGE = 5;

// Test Data
const testRequests = [
    {
        id: 1,
        username: "Фролова Анастасия",
        type: "Свалка",
        coordinates: "55.751244, 37.618423",
        date: "16 ноября, 21:43",
        photo: require("./photo_2024-11-17_05-14-27.jpg"),
        status: "Рассматривается",
        assigned_worker_id: 1,
        description: "h erthert he ty hetyh h eth",
    },
    {
        id: 2,
        username: "Ершов Кирилл",
        type: "Не убрано",
        coordinates: "60.234567, 30.123456",
        date: "16 ноября, 21:43",
        photo: require("./photo_2024-11-17_05-59-17.jpg"),
        status: "Выполнено",
        assigned_worker_id: 1,
        description: "h erthert he ty hetyh h eth",
    },
    {
        id: 3,
        username: "Неизвестный пользователь",
        type: "Мусор на дороге",
        coordinates: "59.934280, 30.335098",
        date: "16 ноября, 21:43",
        photo: require("./photo_2024-11-17_08-05-41.jpg"),
        status: "Рассматривается",
        assigned_worker_id: 1,
        description: "h erthert he ty hetyh h eth",
    },
    {
        id: 4,
        username: "Иванов Иван",
        type: "Не убрано",
        coordinates: "59.123456, 30.654321",
        date: "16 ноября, 21:43",
        photo: require("./photo_2024-11-17_05-14-09.jpg"),
        status: "Выполнено",
        assigned_worker_id: 1,
        description: "h erthert he ty hetyh h eth",
    },
    {
        id: 5,
        username: "Ершов Кирилл",
        type: "Не убрано",
        coordinates: "60.234567, 30.123456",
        date: "16 ноября, 21:43",
        photo: require("./photo_2024-11-17_08-14-40.jpg"),
        status: "Выполнено",
        assigned_worker_id: 1,
        description: "h erthert he ty hetyh h eth",
    },
    {
        id: 6,
        username: "Петров Петр",
        type: "Мусор на дороге",
        coordinates: "60.234567, 30.123456",
        date: "16 ноября, 21:43",
        photo: require("./photo_2024-11-17_05-14-09.jpg"),
        status: "Рассматривается",
        assigned_worker_id: 1,
        description: "h erthert he ty hetyh h eth",
    },
];

const RequestsPage: React.FC = () => {
    const [currentPage, setCurrentPage] = useState<number>(1);
    const [currentRequests, setCurrentRequests] = useState<any[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [selectedRequest, setSelectedRequest] = useState<any | null>(null);

    const totalPages = Math.ceil(testRequests.length / ITEMS_PER_PAGE);

    const handlePageChange = (direction: "prev" | "next") => {
        if (direction === "prev" && currentPage > 1) {
            setCurrentPage((prev) => prev - 1);
        } else if (direction === "next" && currentPage < totalPages) {
            setCurrentPage((prev) => prev + 1);
        }
    };

    const getCurrentPageRequests = (page: number) => {
        const startIndex = (page - 1) * ITEMS_PER_PAGE;
        const endIndex = page * ITEMS_PER_PAGE;
        return testRequests.slice(startIndex, endIndex);
    };

    const handleSelectRequest = (id: number) => {
        const request = testRequests.find((req) => req.id === id);
        setSelectedRequest(request || null);
    };

    const handleClearSelection = () => {
        setSelectedRequest(null);
    };

    useEffect(() => {
        setIsLoading(true);
        setCurrentRequests([]);
        const timeout = setTimeout(() => {
            const newRequests = getCurrentPageRequests(currentPage);
            setCurrentRequests(newRequests);
            setIsLoading(false);
        }, 300);

        return () => clearTimeout(timeout);
    }, [currentPage]);

    return (
        <div className={styles.requestsPage}>
            <h1 className={styles.title}>Заявки</h1>
            <div className={styles.requestListContainer}>
                {isLoading || currentRequests.length === 0 ? (
                    <div className={styles.loading}>Загрузка...</div>
                ) : (
                    <RequestList
                        requests={currentRequests}
                        onSelectRequest={handleSelectRequest}
                    />
                )}
            </div>
            <div className={styles.pagination}>
                <button
                    onClick={() => handlePageChange("prev")}
                    disabled={currentPage === 1}
                    className={styles.arrow}
                >
                    &#8592; Пред
                </button>
                <span className={styles.currentPage}>
                    {currentPage} из {totalPages}
                </span>
                <button
                    onClick={() => handlePageChange("next")}
                    disabled={currentPage === totalPages}
                    className={styles.arrow}
                >
                    След &#8594;
                </button>
            </div>
            <div className={styles.requestDetailsContainer}>
                {selectedRequest ? (
                    <>
                        <RequestDetails request={selectedRequest} />
                        <button onClick={handleClearSelection} className={styles.clearButton}>
                            Очистить
                        </button>
                    </>
                ) : (
                    <div className={styles.emptyState}>
                        Здесь будет отображаться выбранная заявка
                    </div>
                )}
            </div>
        </div>
    );
};

export default RequestsPage;
