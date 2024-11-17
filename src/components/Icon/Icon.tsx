import React from 'react';

interface IconProps {
  src: string; // Путь к SVG
  width?: string | number; // Ширина иконки
  height?: string | number; // Высота иконки
  color?: string; // Цвет иконки
  className?: string; // Дополнительные классы
}

const Icon: React.FC<IconProps> = ({ src, width = 24, height = 24, color = 'inherit', className }) => {
  return (
    <img
      src={src}
      alt="icon"
      style={{ width, height, color }}
      className={className}
    />
  );
};

export default Icon;
