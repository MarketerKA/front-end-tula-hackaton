import React from "react";
import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    Legend,
    ResponsiveContainer,
    LineChart,
    Line,
    CartesianGrid,
} from "recharts";
import styles from "./DashBoardPage.module.scss";

// Данные для графиков
const barData = [
    { date: "07.11", район1: 30, район2: 50 },
    { date: "08.11", район1: 40, район2: 45 },
    { date: "09.11", район1: 25, район2: 30 },
    { date: "10.11", район1: 55, район2: 60 },
    { date: "11.11", район1: 40, район2: 35 },
    { date: "12.11", район1: 50, район2: 70 },
    { date: "13.11", район1: 45, район2: 55 },
    { date: "14.11", район1: 35, район2: 40 },
    { date: "15.11", район1: 50, район2: 60 },
];

const lineData = [
    { date: "07.11", count: 5 },
    { date: "08.11", count: 10 },
    { date: "09.11", count: 8 },
    { date: "10.11", count: 20 },
    { date: "11.11", count: 15 },
    { date: "12.11", count: 5 },
    { date: "13.11", count: 10 },
    { date: "14.11", count: 8 },
    { date: "15.11", count: 20 },
];

const peakPeriodsData = [
    { time: "4:00", value: 5 },
    { time: "8:00", value: 20 },
    { time: "12:00", value: 15 },
    { time: "16:00", value: 40 },
    { time: "18:00", value: 30 },
    { time: "22:00", value: 25 },
];

// Компонент для временных значений
const TimeValues: React.FC = () => (
    <div className={styles.timeValues}>
        <h3>Временные значения</h3>
        <div className={styles.timeCard}>
            <div className={styles.circle} style={{ backgroundColor: "#C8F4F9" }}></div>
            <div>
                <p>Среднее время реакции</p>
                <h2>3,5 часа</h2>
            </div>
        </div>
        <div className={styles.timeCard}>
            <div className={styles.circle} style={{ backgroundColor: "#FFD8D8" }}></div>
            <div>
                <p>Среднее время выполнения</p>
                <h2>2 дня</h2>
            </div>
        </div>
    </div>
);

// График выявления и устранения свалок
const DetectionChart: React.FC = () => (
    <div className={styles.chart}>
        <h3>Обнаружение и устранение свалок <span className={styles.link}>по дням</span></h3>
        <ResponsiveContainer width="100%" height={300}>
            <LineChart data={lineData}>
                <CartesianGrid stroke="#ccc" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Line
                    type="monotone"
                    dataKey="count"
                    stroke="#2d60ff"
                    dot={{ stroke: "#ff80aa", strokeWidth: 2, fill: "#fff", r: 5 }}
                />
            </LineChart>
        </ResponsiveContainer>
    </div>
);

// График сравнения районов
const RegionComparison: React.FC = () => (
    <div className={styles.chart}>
        <h3>Сравнение районов</h3>
        <ResponsiveContainer width="100%" height={300}>
            <BarChart data={barData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="район1" fill="#2d60ff" barSize={20} />
                <Bar dataKey="район2" fill="#ff80aa" barSize={20} />
            </BarChart>
        </ResponsiveContainer>
    </div>
);

// График идентификации пиковых периодов
const PeakPeriodsChart: React.FC = () => (
    <div className={styles.chart}>
        <h3>Идентификация пиковых периодов</h3>
        <ResponsiveContainer width="100%" height={300}>
            <LineChart data={peakPeriodsData}>
                <CartesianGrid stroke="#ccc" />
                <XAxis dataKey="time" />
                <YAxis />
                <Tooltip />
                <Line
                    type="monotone"
                    dataKey="value"
                    stroke="#ffa726"
                    dot={{ stroke: "#ffa726", strokeWidth: 2, fill: "#fff", r: 5 }}
                />
            </LineChart>
        </ResponsiveContainer>
    </div>
);

// Главный компонент
const DashBoardPage: React.FC = () => {
    return (
        <div className={styles.dashboard}>
            <div className={styles.header}>
                <h1>Общая статистика за период 07.11 - 15.11</h1>
                <button className={styles.searchButton}>Найти</button>
            </div>
            <div className={styles.stats}>
                <div className={styles.statCard}>
                    <p>Выявленные свалки</p>
                    <h2>28</h2>
                </div>
                <div className={styles.statCard}>
                    <p>Устраненные свалки</p>
                    <h2>12</h2>
                </div>
                <div className={styles.statCard}>
                    <p>% устранения</p>
                    <h2>79,6%</h2>
                </div>
                <div className={styles.statCard}>
                    <p>Активные заявки</p>
                    <h2>12</h2>
                </div>
            </div>

            <div className={styles.row}>
                <TimeValues />
                <RegionComparison />
            </div>

            <div className={styles.row}>
                <DetectionChart />
                <PeakPeriodsChart />
            </div>
        </div>
    );
};

export default DashBoardPage;
