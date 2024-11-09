// CarModel.jsx
import { useGLTF } from '@react-three/drei';

function CarModel({ url }) {
  const { scene } = useGLTF(url);
  
  // Ajusta la posición y la escala del coche si es necesario
  // scene.position.set(3.9, -0.68, -2.7); // Ajusta según sea necesario ferrari
  scene.position.set(3, -0.68, -1.4);
    scene.scale.set(1, 1, 1); // Ajusta según sea necesario
    scene.rotation.set(0, Math.PI / -4.8, 0);

  return <primitive object={scene} />;
}

export default CarModel;




