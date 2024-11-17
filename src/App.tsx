import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import RequestsPage from "./pages/RequestsPage";
import NotificationsPage from "./pages/NotificationsPage";
import SettingsPage from "./pages/SettingsPage";
import DashBoardPage from "./pages/DashBoardPage";
import WorkerRequestPage from "./pages/WorkerRequestPage"; // Import the new page

const App: React.FC = () => {
    return (
        <Router>
            <NavBar />
            <Routes>
                <Route path="/" element={<DashBoardPage />} />
                <Route path="/requests" element={<RequestsPage />} />
                <Route path="/notifications" element={<NotificationsPage />} />
                <Route path="/settings" element={<SettingsPage />} />
                <Route path="/worker-requests" element={<WorkerRequestPage />} /> {/* New route */}
            </Routes>
        </Router>
    );
};

export default App;
