import React from 'react';
import './LearningPathDisplay.css';
import { FaLightbulb, FaTasks, FaBullseye, FaYoutube, FaCheckCircle } from 'react-icons/fa';
import YouTube from 'react-youtube';

function LearningPathDisplay({ data }) {
  const path = data.learning_path;
  const rationale = data.rationale;

  // Opsi untuk video player yang disematkan
  const playerOptions = {
    height: '360',
    width: '100%', // Lebar akan diatur oleh CSS container
    playerVars: {
      // https://developers.google.com/youtube/player_parameters
      autoplay: 0,
      modestbranding: 1,
    },
  };

  if (!path || path.length === 0) {
    return null; // Jangan tampilkan apa-apa jika tidak ada data
  }

  return (
    <div className="results-container">
      <h2>Jalur Belajar Personal Anda ({path.length} Minggu)</h2>
      
      <div className="rationale-box">
        <strong><FaLightbulb /> Rekomendasi AI:</strong>
        <p>{rationale}</p>
      </div>

      {path.map((week) => (
        <div key={week.week} className="week-card">
          <div className="week-header">
            <h3>Minggu {week.week}: {week.goal}</h3>
          </div>
          <div className="week-content">
            <h4><FaTasks /> Topik yang Perlu Dikuasai:</h4>
            <ul>
              {week.topics.map((topic, index) => (
                <li key={index}>
                  {/* Mengelompokkan ikon dan nama topik */}
                  <div className="topic-name-container">
                    <FaCheckCircle className="topic-icon" />
                    <span>{topic.name}</span>
                  </div>

                  {/* Menampilkan link YouTube jika ada */}
                  {topic.youtube_suggestion && (
                    <a 
                      href={topic.youtube_suggestion.url} 
                      target="_blank" 
                      rel="noopener noreferrer" 
                      className="youtube-link"
                      title={`Tonton: ${topic.youtube_suggestion.title}`}
                    >
                      <FaYoutube /> Tonton Video
                    </a>
                  )}
                </li>
              ))}
            </ul>

            {/* Bagian Ide Proyek Mingguan */}
            <h4><FaBullseye /> Ide Proyek Mingguan:</h4>
            {/* Tampilkan teks ide proyek */}
            <p>{week.project_idea.text}</p>
            
            {/* Jika ada video, tampilkan video player */}
            {week.project_idea.video && (
              <div className="video-player-container">
                <p className="video-player-title">Tonton Video Tutorial Proyek:</p>
                <YouTube 
                  videoId={week.project_idea.video.videoId} 
                  opts={playerOptions} 
                />
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}

export default LearningPathDisplay;