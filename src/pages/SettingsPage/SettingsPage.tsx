import React, { useState } from "react";
import styles from "./SettingsPage.module.scss";

const SettingsPage: React.FC = () => {
    const [notifications, setNotifications] = useState<boolean>(true);
    const [privacy, setPrivacy] = useState<string>("public");

    return (
        <div className={styles.page}>
            <div className={styles.container}>
                <h1>Настройки</h1>
                <div className={styles.section}>
                    <h2>Общие настройки</h2>
                    <div className={styles.item}>
                        <label htmlFor="username">Имя пользователя:</label>
                        <input type="text" id="username" placeholder="Введите имя пользователя" />
                    </div>
                    <div className={styles.item}>
                        <label htmlFor="language">Язык:</label>
                        <select id="language">
                            <option value="ru">Русский</option>
                            <option value="en">English</option>
                            <option value="fr">Français</option>
                        </select>
                    </div>
                </div>

                <div className={styles.section}>
                    <h2>Уведомления</h2>
                    <div className={styles.item}>
                        <label>Получать уведомления:</label>
                        <label className={styles.switch}>
                            <input
                                type="checkbox"
                                checked={notifications}
                                onChange={() => setNotifications(!notifications)}
                            />
                            <span className={styles.slider}></span>
                        </label>
                    </div>
                </div>

                <div className={styles.section}>
                    <h2>Приватность</h2>
                    <div className={styles.item}>
                        <label>Профиль:</label>
                        <select
                            value={privacy}
                            onChange={(e) => setPrivacy(e.target.value)}
                        >
                            <option value="public">Публичный</option>
                            <option value="private">Приватный</option>
                        </select>
                    </div>
                </div>

                <button className={styles.saveButton}>Сохранить изменения</button>
            </div>
        </div>
    );
};

export default SettingsPage;
