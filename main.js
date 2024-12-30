document.addEventListener('DOMContentLoaded', () => {
    const pentagramDiv = document.getElementById('pentagram');
    const subtopicsDiv = document.getElementById('subtopics');
    const contentDiv = document.getElementById('content');
    const mainJsContentDiv = document.getElementById('main-js-content');

    // Display main.js content
    fetch('/static/js/main.js')
        .then(response => response.text())
        .then(code => {
            mainJsContentDiv.textContent = code;
        });

    // Set up Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, pentagramDiv.clientWidth / pentagramDiv.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(pentagramDiv.clientWidth, pentagramDiv.clientHeight);
    pentagramDiv.appendChild(renderer.domElement);

    // Create pentagram
    const geometry = new THREE.BufferGeometry();
    const vertices = [];
    const radius = 1;
    for (let i = 0; i < 5; i++) {
        const angle = (i * 4 * Math.PI) / 5;
        vertices.push(
            radius * Math.cos(angle), radius * Math.sin(angle), 0,
            0, 0, 0
        );
    }
    geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
    const material = new THREE.LineBasicMaterial({ color: 0x3498db });
    const pentagram = new THREE.LineSegments(geometry, material);
    scene.add(pentagram);

    camera.position.z = 5;

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        pentagram.rotation.x += 0.01;
        pentagram.rotation.y += 0.01;
        renderer.render(scene, camera);
    }
    animate();

    // Event listener for pentagram clicks
    renderer.domElement.addEventListener('click', (event) => {
        const rect = renderer.domElement.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        const y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        const raycaster = new THREE.Raycaster();
        raycaster.setFromCamera({ x, y }, camera);

        const intersects = raycaster.intersectObject(pentagram);

        if (intersects.length > 0) {
            const topics = ['Science', 'History', 'Art', 'Technology', 'Philosophy'];
            const clickedIndex = Math.floor(Math.random() * topics.length);
            const topic = topics[clickedIndex];

            fetch(`/subtopics/${topic}`)
                .then(response => response.json())
                .then(subtopics => {
                    subtopicsDiv.innerHTML = '';
                    subtopics.forEach(subtopic => {
                        const subtopicBtn = document.createElement('button');
                        subtopicBtn.textContent = subtopic;
                        subtopicBtn.addEventListener('click', () => {
                            fetch(`/content/${topic}/${subtopic}`)
                                .then(response => response.json())
                                .then(data => {
                                    contentDiv.innerHTML = `<h2>${subtopic}</h2><p>${data.content}</p>`;
                                });
                        });
                        subtopicsDiv.appendChild(subtopicBtn);
                    });
                });
        }
    });
});