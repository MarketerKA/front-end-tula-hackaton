const testRequests = [
    {
        id: 1,
        username: "Фролова Анастасия",
        type: "dirt",
        coordinates: "55.751244, 37.618423",
        created_at: "16 ноября, 21:43",
        image: "trash_project/media/trash_cans/133500.jpg",
        description: "Описание заявки 1",
        status: "in_progress",
        assigned_worker_id: 1,
    },
    {
        id: 2,
        username: "Ершов Кирилл",
        type: "dirt",
        coordinates: "60.234567, 30.123456",
        created_at: "16 ноября, 21:43",
        image: "trash_project/media/trash_cans/133501.jpg",
        description: "Описание заявки 2",
        status: "completed",
        assigned_worker_id: 2,
    },
    {
        id: 3,
        username: null,
        type: "road_trash",
        coordinates: "59.934280, 30.335098",
        created_at: "16 ноября, 21:43",
        image: "trash_project/media/trash_cans/133502.jpg",
        description: "Описание заявки 3",
        status: "in_progress",
        assigned_worker_id: 3,

    },
];

export default testRequests;
