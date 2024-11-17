import React from "react";
import styles from "./NavBar.module.scss";
import { NavLink } from "react-router-dom";
import HomeIcon from "./icons/HomeIcon";
import RequestsIcon from "./icons/RequestsIcon";
import NotificationsIcon from "./icons/NotificationsIcon";
import SettingsIcon from "./icons/SettingsIcon";
import ProfileIcon from "../../assets/icons/profileIcon.svg";

export const NavBar: React.FC = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>ИС «ЭкоСкан»</div>
      <ul className={styles.menu}>
        <li className={styles.menuItem}>
          <NavLink
              to="/"
              className={({isActive}) => (isActive ? styles.active : "")}
          >
            <span className={styles.icon}>
              <HomeIcon/>
            </span>
            <span>Дашборд</span>
          </NavLink>
        </li>
        <li className={styles.menuItem}>
          <NavLink
              to="/requests"
              className={({isActive}) => (isActive ? styles.active : "")}
          >
            <span className={styles.icon}>
              <RequestsIcon/>
            </span>
            <span>Заявки</span>
          </NavLink>
        </li>
        <li className={styles.menuItem}>
          <NavLink
              to="/notifications"
              className={({isActive}) => (isActive ? styles.active : "")}
          >
            <span className={styles.icon}>
              <NotificationsIcon/>
            </span>
            <span>Уведомления</span>
          </NavLink>
        </li>
        <li className={styles.menuItem}>
          <NavLink
              to="/settings"
              className={({isActive}) => (isActive ? styles.active : "")}
          >
            <span className={styles.icon}>
              <SettingsIcon/>
            </span>
            <span>Настройки</span>
          </NavLink>
        </li>
        <li className={styles.menuItem}>
          <NavLink
              to="/worker-requests"
              className={({isActive}) => (isActive ? styles.active : "")}
          >
        <span className={styles.icon}>
            {/* Replace WorkerIcon with your desired icon */}
        </span>
            <span>Для сотрудника</span>
          </NavLink>
        </li>
      </ul>
      <div className={styles.profile}>
        <img src={ProfileIcon} alt="Profile" className={styles.profileIcon}/>
      </div>
    </nav>
  );
};

export default NavBar;
