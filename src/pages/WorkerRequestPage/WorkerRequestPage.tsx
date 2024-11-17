import React, { useState, useEffect } from "react";
import axios from "axios";
import styles from "./WorkerRequestPage.module.scss";

const API_URL = "http://152.42.239.85:1000/api/worker/requests/"; // API для запросов работника

const WorkerRequestPage: React.FC = () => {
    const [requestData, setRequestData] = useState({
        type: "",
        description: "",
        beforePhoto: null,
        afterPhoto: null,
    });

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = e.target;
        setRequestData((prev) => ({ ...prev, [name]: value }));
    };

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, files } = e.target;
        if (files && files.length > 0) {
            setRequestData((prev) => ({ ...prev, [name]: files[0] }));
        }
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        // Form data for the request
        const formData = new FormData();
        formData.append("type", requestData.type);
        formData.append("description", requestData.description);
        if (requestData.beforePhoto) formData.append("before_photo", requestData.beforePhoto);
        if (requestData.afterPhoto) formData.append("after_photo", requestData.afterPhoto);

        try {
            const response = await fetch("http://your-backend-url/api/worker-requests/", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                alert("Заявка успешно отправлена!");
                setRequestData({
                    type: "",
                    description: "",
                    beforePhoto: null,
                    afterPhoto: null,
                });
            } else {
                alert("Ошибка при отправке заявки.");
            }
        } catch (error) {
            console.error("Ошибка при отправке запроса:", error);
            alert("Ошибка при отправке заявки.");
        }
    };

    return (
        <div className={styles.workerRequestPage}>
            <h1>Создание заявки</h1>
            <form onSubmit={handleSubmit} className={styles.form}>
                <div className={styles.formGroup}>
                    <label htmlFor="type">Тип заявки</label>
                    <input
                        type="text"
                        id="type"
                        name="type"
                        value={requestData.type}
                        onChange={handleInputChange}
                        placeholder="Например, Свалка"
                        required
                    />
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="description">Описание</label>
                    <textarea
                        id="description"
                        name="description"
                        value={requestData.description}
                        onChange={handleInputChange}
                        placeholder="Введите описание..."
                        required
                    ></textarea>
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="beforePhoto">Фото ДО</label>
                    <input
                        type="file"
                        id="beforePhoto"
                        name="beforePhoto"
                        onChange={handleFileChange}
                        accept="image/*"
                        required
                    />
                </div>
                <div className={styles.formGroup}>
                    <label htmlFor="afterPhoto">Фото ПОСЛЕ</label>
                    <input
                        type="file"
                        id="afterPhoto"
                        name="afterPhoto"
                        onChange={handleFileChange}
                        accept="image/*"
                        required
                    />
                </div>
                <button type="submit" className={styles.submitButton}>
                    Отправить заявку
                </button>
            </form>
        </div>
    );
};

export default WorkerRequestPage;